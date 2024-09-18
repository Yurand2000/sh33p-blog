from flask import Flask
from .local_config import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route("/robots.txt")
def robots():
    return "Hello World from Robots"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='localhost', debug=True, port=SERVER_PORT)