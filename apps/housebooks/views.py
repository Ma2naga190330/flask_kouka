from flask import Flask,render_template,Blueprint,redirect,url_for
from apps.app import db
from apps.housebooks.models import MoneyBooks
from apps.housebooks.forms import MoneyBookForm
from sqlalchemy import func
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
    total = 0
    moneybooks = MoneyBooks.query.all()
    total = db.session.query(func.sum(MoneyBooks.price)).first()
    return render_template("housebooks/read.html", moneybooks=moneybooks, total=total[0])

@hb.route("/create", methods=["GET","POST"])
def create():
    form = MoneyBookForm()
    if form.validate_on_submit():
        moneybooks = MoneyBooks(
            account_id = form.account_id.data,
            comment = form.comment.data,
            price=form.price.data
        )
        db.session.add(moneybooks)
        db.session.commit()
        return redirect(url_for("housebooks.read"))
    return render_template("housebooks/create.html",form=form)