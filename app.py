from flask import Flask, render_template, Blueprint
from archive import archive

pp = Blueprint(
    "parking-proliferation",
    __name__,
    template_folder=r"pages/archive/posts/parking-proliferation/build",
    static_url_path="",
    static_folder=r"pages\archive\posts\parking-proliferation\build",
)

app = Flask(__name__, template_folder="pages", static_folder="static")


@app.route("/")
def index():
    return render_template("/index/home.html")


@app.route("/about")
def about():
    return render_template("about/about.html")


@app.route("/archive")
def posts():
    return render_template("archive/archive.html", my_archive=archive())


@app.route("/archive/<post_title>")
def post(post_title):
    return render_template(f"archive/posts/{post_title}.html")



@pp.route("/archive/parking-proliferation")
def parking_proliferation():
    return render_template("index.html")


app.register_blueprint(pp)
