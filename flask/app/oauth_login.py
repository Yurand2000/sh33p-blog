import requests
from flask import Request, session

class LoginInfo:
    def __init__(self, login_data):
        if not login_data['email_verified']:
            return None
        
        self.access_token = login_data['access_token']
        self.id_token = login_data['id_token']
        self.expires_in = login_data['expires_in']
        self.scopes = login_data['scope']
        self.sub = login_data['sub']
        self.name = login_data['name']
        self.first_name = login_data['given_name']
        self.last_name = login_data['family_name']
        self.picture = login_data['picture']
        self.email = login_data['email']

    def __str__(self):
        return f"LoginInfo for {self.name}, email: {self.email}"

class OauthLoginHandler:
    def get_login_uri(self, login_hint: str | None = None) -> str:
        pass

    def on_login_callback(self, request: Request) -> LoginInfo | None:
        pass

class GoogleLogin(OauthLoginHandler):
    def __init__(self, callback_uri: str):
        import os
        from oauthlib.oauth2 import WebApplicationClient

        self.GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
        self.GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
        self.callback_uri = callback_uri
        self.login_scopes = ['openid', 'email', 'profile']

        self.client = WebApplicationClient(self.GOOGLE_CLIENT_ID)

    def __get_google_provider_cfg():
        GOOGLE_DISCOVERY_URL = (
            "https://accounts.google.com/.well-known/openid-configuration"
        )
        return requests.get(GOOGLE_DISCOVERY_URL).json()

    def get_login_uri(self, request: Request, login_hint: str | None = None) -> str:
        import hashlib, os
        csrf_token = hashlib.sha256(os.urandom(1024)).hexdigest()
        session['csrf_token'] = csrf_token
        google_cfg = GoogleLogin.__get_google_provider_cfg()

        host_uri = request.host
        if login_hint is not None:
            return self.client.prepare_request_uri(
                google_cfg['authorization_endpoint'],
                redirect_uri = f"https://{host_uri}/{self.callback_uri}",
                scope = self.login_scopes,
                state = csrf_token
            )
        else:
            return self.client.prepare_request_uri(
                google_cfg['authorization_endpoint'],
                redirect_uri = f"https://{host_uri}/{self.callback_uri}",
                scope = self.login_scopes,
                state = csrf_token,
                login_hint = login_hint
            )
    
    def on_login_callback(self, request: Request) -> LoginInfo | None:
        google_cfg = GoogleLogin.__get_google_provider_cfg()

        # check csrf token
        request_csrf_token = request.args.get('state')
        csrf_token = session.get('csrf_token')
        if csrf_token is not None:
            session.pop('csrf_token')

        if request_csrf_token != csrf_token:
            return None

        # get access tokens
        auth_code = request.args.get('code')
        query_str = request.url.removeprefix(request.base_url)
        host_uri = request.host
        token_url, headers, body = self.client.prepare_token_request(
            google_cfg['token_endpoint'],
            authorization_response = f"https://{host_uri}/{self.callback_uri}{query_str}",
            redirect_url = f"https://{host_uri}/{self.callback_uri}",
            code = auth_code
        )

        token_response = requests.post(
            token_url,
            headers = headers,
            data = body,
            auth = (self.GOOGLE_CLIENT_ID, self.GOOGLE_CLIENT_SECRET),
        )

        tokens = self.client.parse_request_body_response(token_response.content)

        userinfo_endpoint = google_cfg["userinfo_endpoint"]
        uri, headers, body = self.client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)
        return LoginInfo(tokens | userinfo_response.json())