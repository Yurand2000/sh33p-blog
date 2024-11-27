import os
from flask import Flask, render_template
from config import *
from templates import *
from articles import *

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error = None):
    return render_skeleton("404...", render_template("404.html"))

@app.route("/")
def index():
    articles = ''.join(render_articles_previews())
    posts = render_template("articles/posts.html", articles= articles)
    return render_skeleton("Sheep Blog", content= posts)

@app.route("/about")
def about():
    return article("about_sheep", False)

@app.route("/amenity")
def amenity():
    amenity = render_template("amenities/origin.html")
    content = render_template("amenity.html", amenity = amenity)
    return render_skeleton("Amenity", content= content)

@app.route('/articles/<article>')
def article(article, skip_hidden = True):
    article = render_article(article, skip_hidden)
    if article is None:
        return not_found()
    else:
        return render_skeleton(article['metadata']['title'], content= article['article'])
    
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