from flask import Flask, render_template
from .local_config import *
app = Flask(__name__)

HOMEPAGE = "localhost:"+str(SERVER_PORT)

@app.errorhandler(404)
def not_found(error = None):
    return render_template("404.html", head = head("404..."), header = header(), footer = footer())

@app.route("/")
def index():
    return render_template("index.html", head = head("Server-Grossi"), header = header(), footer = footer())

@app.route("/about")
def about():
    return render_template("about.html", head = head("About"), header = header(), footer = footer())

@app.route("/amenity")
def amenity():
    amenity = render_template("defaults/amenity.html")
    return render_template("amenity.html", head = head("Amenity"), header = header(), footer = footer(), amenity = amenity)

def head(title, other = ""):
    return render_template("generic/head.html", title = title, other = other)

def header():
    return render_template("generic/header.html", homepage = HOMEPAGE)

def footer():
    return render_template("generic/footer.html", homepage = HOMEPAGE)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='localhost', debug=True, port=SERVER_PORT)