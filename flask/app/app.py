import os
import json
from flask import Flask, render_template
from templates import *
from articles import *
from login import *

def load_config():
    with open("/blog/data/config.json", "r") as f:
        return json.loads(f.read())

app = Flask(__name__)
app_config = load_config()

client_handler = ClientHandler('https://127.0.0.1:5000/login/callback')

@app.errorhandler(404)
def not_found(error = None):
    return render_skeleton("404...", render_template("404.html"), app_config)

@app.route("/")
def index():
    articles = ''.join(render_articles_previews())
    posts = render_template("articles/posts.html", articles= articles)
    return render_skeleton(app_config["blog-name"], posts, app_config)

@app.route("/about")
def about():
    return article(app_config['about-page'], False)

@app.route("/amenity")
def amenity():
    amenity = render_template("amenities/origin.html")
    content = render_template("amenity.html", amenity = amenity)
    return render_skeleton("Amenity", content, app_config)

@app.route('/articles/<article>')
def article(article, skip_hidden = True):
    article = render_article(article, skip_hidden)
    if article is None:
        return not_found()
    else:
        return render_skeleton(article['metadata']['title'], article['article'], app_config)
    
@app.route('/about/<username>')
def about_user(username):
    return article(f"about_{username}", False)

@app.route('/flask-health-check')
def flask_health_check():
	return "success"

@app.route('/login')
def login_page():
    google_login_uri = client_handler.login()
    content = render_template("login/login.html", uri= google_login_uri)
    return render_skeleton("Login", content, app_config)

@app.route('/login/callback')
def login_callback():
    from flask import request
    print(client_handler.login_callback(request))

if __name__ == "__main__":
    import os, sys
    os.chdir(os.path.dirname(sys.argv[0]))
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)