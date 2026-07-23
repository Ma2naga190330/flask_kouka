from flask import Flask,render_template,Blueprint,redirect,url_for

cs = Blueprint(
    "categories",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@cs.route("/")
def index():
    return render_template("category_sort/index.html")