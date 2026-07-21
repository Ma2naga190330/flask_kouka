from flask import Flask,render_template,Blueprint

hb = Blueprint(
    "housebooks",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@hb.route("/")
def index():
    return render_template("housebooks/index.html")