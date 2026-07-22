from flask import Flask,render_template,Blueprint,redirect,url_for
from apps.app import db
from apps.housebooks.models import MoneyBooks
from apps.housebooks.forms import MoneyBookForm,DeleteForm
from sqlalchemy import func
from flask_wtf import csrf
from flask_login import login_required
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
    form = DeleteForm()
    total = 0
    moneybooks = MoneyBooks.query.all()
    total = db.session.query(func.sum(MoneyBooks.price)).first()
    return render_template("housebooks/read.html", moneybooks=moneybooks, total=total[0], delform = form)

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

@hb.route("/read/delete/<moneybooks_id>",methods=["GET","POST"])
@login_required
def delete(moneybooks_id):
    print("------------------------>"+moneybooks_id)
    moneybooks = MoneyBooks.query.filter_by(id=moneybooks_id).first()
    print(moneybooks)
    db.session.delete(moneybooks)
    db.session.commit()
    return redirect(url_for("housebooks.read"))

@hb.route("/read/update/<int:moneybooks_id>", methods=["GET","POST"])
def update(moneybooks_id):
    form = MoneyBookForm()
    moneybooks = MoneyBooks.query.filter_by(id=moneybooks_id).first()

    if form.validate_on_submit():
        moneybooks.account_id = form.account_id.data
        moneybooks.comment = form.comment.data
        moneybooks.price=form.price.data
        db.session.add(moneybooks)
        db.session.commit()
        return redirect(url_for("housebooks.read"))
    return render_template("housebooks/update.html",moneybooks=moneybooks,form=form)