from flask import render_template, Blueprint

bp = Blueprint("bp", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/posts")
def posts():
    return render_template("posts.html")


@bp.route("/post/<post_title>")
def post(post_title):
    return render_template(post_title)
