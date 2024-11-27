from flask import render_template
from config import *

def render_skeleton(title, content):
    return render_template(
        "skeleton.html",
        head = head(title),
        header = header(),
        footer = footer(),
        content = content
    )

def head(title, other = ""):
    return render_template("generic/head.html", title = title, other = other)

def header():
    return render_template("generic/header.html", homepage = HOMEPAGE)

def footer():
    return render_template("generic/footer.html", homepage = HOMEPAGE)