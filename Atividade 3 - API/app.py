import site
from flask import Flask, redirect, render_template

site = Flask(__name__)

@site.route("/")
def index():
    return redirect("/static/index.html")