from flask import Blueprint, redirect, abort
from globals import user_management
from oauth_login import GoogleLogin

login_bp = Blueprint("login_pages", __name__)
oauth = GoogleLogin("login/callback")

@login_bp.route('/login')
def login_page():
    from flask import request
    if not user_management.is_logged_in():
        login_uri = oauth.get_login_uri(request)
        return redirect(login_uri)
    else:
        return redirect("/")

@login_bp.route('/login/callback')
def login_callback():
    from flask import request
    login_data = oauth.on_login_callback(request)

    if login_data is not None:
        user_management.login(login_data)
        return redirect("/")
    else:
        return abort(404)
    
@login_bp.route('/logout', methods=["POST"])
def logout():
    user_management.logout()
    return redirect("/")