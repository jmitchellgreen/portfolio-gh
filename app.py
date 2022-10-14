from flask import Flask, render_template
from archive import archive

app = Flask(__name__, template_folder="pages")


@app.route("/")
def index():
    return render_template("index/index.html")


@app.route("/about")
def about():
    return render_template("about/about.html")


@app.route("/archive")
def posts():
    print(archive())  # pass to archive.html
    return render_template("archive/archive.html")


@app.route("/archive/<post_title>")
def post(post_title):
    return render_template(f"archive/{post_title}.html")
