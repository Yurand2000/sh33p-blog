import os
import json
from flask import Flask, render_template, redirect
from templates import *
from articles import *
from oauth_login import *
from session import *
from amenities import *
from pages.settings import *
from globals import *

def load_config():
    global app_config

    with open("/blog/data/config.json", "r") as f:
        config = json.loads(f.read())
        app_config.update((k, config[k]) for k in config.keys())

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
app.register_blueprint(settings_bp)
load_config()

client_handler = GoogleLogin("https://127.0.0.1", "login/callback")
user_management.setup(app, app_config)

@app.errorhandler(404)
def not_found(error = None):
    return render_skeleton("404...", render_template("404.html"))

@app.route("/")
def index():
    articles = ''.join(render_articles_previews())
    posts = render_template("articles/posts.html", articles= articles)
    return render_skeleton(app_config["blog-name"], posts)

@app.route("/about")
def about():
    return article(app_config['about-page'], False)

@app.route("/amenity")
def amenity():
    amenity = get_todays_amenity()
    content = render_template("amenity.html", amenity = amenity)
    return render_skeleton("Amenity", content)

@app.route('/articles/<article>')
def article(article, skip_hidden = True):
    article = render_article(article, skip_hidden)
    if article is None:
        return not_found()
    else:
        return render_skeleton(article['metadata']['title'], article['article'])
    
@app.route('/about/<username>')
def about_user(username):
    return article(f"about_{username}", False)

@app.route('/login')
def login_page():
    if not user_management.is_logged_in():
        google_login_uri = client_handler.get_login_uri()
        return redirect(google_login_uri)
    else:
        return redirect("/")

@app.route('/login/callback')
def login_callback():
    from flask import request
    login_data = client_handler.on_login_callback(request)

    if login_data is not None:
        user_management.login(login_data)
        return redirect("/")
    else:
        return not_found()
    
@app.route('/logout', methods=["POST"])
def logout():
    user_management.logout()
    return redirect("/")

@app.route('/flask-health-check')
def flask_health_check():
	return "success"

if __name__ == "__main__":
    import os, sys
    os.chdir(os.path.dirname(sys.argv[0]))
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)