from flask import Flask,render_template,Blueprint
from apps.app import db
from apps.housebooks.models import MoneyBooks

hb = Blueprint(
    "housebooks",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@hb.route("/")
def index():
    return render_template("housebooks/index.html")

@hb.route("/read", methods=["GET","POST"])
def read():
    moneybook = MoneyBooks.query.all()
    return render_template("housebooks/read.html", moneybooks=moneybook)