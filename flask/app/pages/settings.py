from flask import Blueprint, redirect
from templates import *
from globals import *

settings_bp = Blueprint("settings_page", __name__)

@settings_bp.route("/settings")
def settings():
    if not user_management.is_logged_in():
        return redirect("/")

    return render_skeleton("Settings", "")