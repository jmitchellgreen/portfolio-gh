from flask import Flask, render_template

app = Flask(__name__, template_folder="pages")


@app.route("/")
def index():
    return render_template("index/index.html")


@app.route("/about")
def about():
    return render_template("about/about.html")


@app.route("/archive")
def posts():
    return render_template("archive/archive.html")


@app.route("/archive/<post_title>")
def post(post_title):
    return render_template(post_title)
