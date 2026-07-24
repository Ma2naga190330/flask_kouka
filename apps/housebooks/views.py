from flask import Flask,render_template,Blueprint,redirect,url_for,request
from apps.app import db
from apps.housebooks.models import MoneyBooks,Category
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
@login_required
def read():
    form = DeleteForm()
    moneybooks = MoneyBooks.query.filter_by(deleted=False).all()
    categories = Category.query.all()
    print(categories)
    query_total = db.session.query(func.sum(MoneyBooks.price)).filter(MoneyBooks.deleted == False)
    total = query_total[0][0]
    if total == None:
        total = 0
    return render_template("housebooks/read.html", moneybooks=moneybooks, total=total, delform = form)

@hb.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = MoneyBookForm()
    categories = Category.query.all()
    print(categories)
    category_list=[]
    for c in categories:
        category_list.append((c.id, c.category_name))
    form.category_id.choices = category_list
    if form.validate_on_submit():
        moneybooks = MoneyBooks(
            account_id = form.account_id.data,
            comment = form.comment.data,
            price=form.price.data,
            category_id=form.category_id.data
        )
        db.session.add(moneybooks)
        db.session.commit()
        return redirect(url_for("housebooks.read"))
    return render_template("housebooks/create.html",form=form)

@hb.route("/read/delete/<moneybooks_id>",methods=["GET","POST"])
@login_required
def delete(moneybooks_id):
    print("delete------------------------>"+moneybooks_id)
    moneybooks = MoneyBooks.query.filter_by(id=moneybooks_id).first()
    print(moneybooks)
    moneybooks.deleted = True
    db.session.add(moneybooks)
    db.session.commit()
    return redirect(url_for("housebooks.read"))

@hb.route("/read/update/<int:moneybooks_id>", methods=["GET","POST"])
@login_required
def update(moneybooks_id):
    form = MoneyBookForm()
    moneybooks = MoneyBooks.query.filter_by(id=moneybooks_id).first()
    categories = Category.query.all()
    print(categories)
    category_list=[]
    for c in categories:
        category_list.append((c.id, c.category_name))
        form.category_id.choices = category_list
    if request.method == "GET":
        form.category_id.data = moneybooks.category_id
    if form.validate_on_submit():
        moneybooks.account_id = form.account_id.data
        moneybooks.comment = form.comment.data
        moneybooks.price=form.price.data
        moneybooks.category_id=form.category_id.data
        moneybooks.category
        db.session.add(moneybooks)
        db.session.commit()
        return redirect(url_for("housebooks.read"))
    return render_template("housebooks/update.html",moneybooks=moneybooks,form=form)