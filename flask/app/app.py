import os
import json
from flask import Flask, render_template, redirect
from templates import *
from articles import *
from session import *
from pages.amenities import amenities_bp
from pages.settings import settings_bp
from pages.login import login_bp
from globals import *

def load_config():
    global app_config

    with open("/blog/data/config.json", "r") as f:
        config = json.loads(f.read())
        app_config.update((k, config[k]) for k in config.keys())

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
app.register_blueprint(settings_bp)
app.register_blueprint(login_bp)
app.register_blueprint(amenities_bp)
load_config()

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


@app.route('/flask-health-check')
def flask_health_check():
	return "success"

if __name__ == "__main__":
    import os, sys
    os.chdir(os.path.dirname(sys.argv[0]))
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)