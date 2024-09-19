from flask import Flask, render_template
from .local_config import *
app = Flask(__name__)

HOMEPAGE = "localhost:"+str(SERVER_PORT)

def not_found():
    return render_template("404.html", head = head("Server-Grossi"), header = header(), footer = footer())

@app.route("/")
def index():
    return render_template("index.html", head = head("Server-Grossi"), header = header(), footer = footer())

@app.route("/about")
def about():
    return not_found()

@app.route("/amenity")
def amenity():
    return not_found()

def head(title, other = ""):
    return render_template("head.html", title = title, other = other)

def header():
    return render_template("header.html", homepage = HOMEPAGE)

def footer():
    return render_template("footer.html", homepage = HOMEPAGE)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='localhost', debug=True, port=SERVER_PORT)