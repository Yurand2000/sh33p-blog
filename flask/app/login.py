import requests
import json
from flask import Request, Response

class ClientHandler:
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

    def login(self) -> str:
        google_cfg = ClientHandler.__get_google_provider_cfg()

        print(self.GOOGLE_CLIENT_ID)

        return self.client.prepare_request_uri(
            google_cfg['authorization_endpoint'],
            redirect_uri = self.callback_uri,
            scope = self.login_scopes
        )
    
    def login_callback(self, request: Request):
        auth_code = request.args.get('code')

        google_cfg = ClientHandler.__get_google_provider_cfg()

        token_url, headers, body = self.client.prepare_token_request(
            google_cfg['token_endpoint'],
            authorization_response = request.url,
            redirect_url = request.base_url,
            code = auth_code
        )

        token_response = requests.post(
            token_url,
            headers = headers,
            data = body,
            auth = (self.GOOGLE_CLIENT_ID, self.GOOGLE_CLIENT_SECRET),
        )
        
        self.client.parse_request_body_response(json.dumps(token_response.json()))  

        userinfo_endpoint = google_cfg["userinfo_endpoint"]
        uri, headers, body = self.client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)
        return userinfo_response.json()