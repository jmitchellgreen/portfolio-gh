from flask import Flask, render_template, Blueprint
from archive import archive

pp = Blueprint('parking-proliferation',
                __name__,
                template_folder="pages/archive/posts/parking-proliferation/build",
                static_url_path="",
                static_folder=r"pages\archive\posts\parking-proliferation\build")

app = Flask(__name__,
            template_folder="pages",
            static_folder="static",
            static_url_path="/foo") # bruh idk anymore

app.config['TESTING'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True


@app.route("/")
def index():
    return render_template("/index/home.html")

@app.route("/about")
def about():
    return render_template("about/about.html")

@app.route("/about/resume")
def resume():
    return render_template("about/J Mitchell Green Resume.html")

@app.route("/archive")
def posts():
    return render_template("archive/archive.html", my_archive=archive())

@app.route("/archive/<post_title>")
def post(post_title):
    return render_template(f"archive/posts/{post_title}.html")

@pp.route("/parking-proliferation")
def parking_proliferation():
    return render_template("index.html")


app.register_blueprint(pp)