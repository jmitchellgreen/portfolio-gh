from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts")
def posts():
    return render_template("posts.html")


@app.route("/posts/<post_title>")
def post(post_title):
    return render_template(post_title)
