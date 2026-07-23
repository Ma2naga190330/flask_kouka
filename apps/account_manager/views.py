from flask import Blueprint,render_template,url_for,flash,request,redirect
from apps.account_manager.forms import SignupForm,LoginForm
# signup
from apps.account_manager.models import Account,Permission
# db
from apps.app import db
# login
from flask_login import login_user,logout_user

ac = Blueprint(
    "accounts",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@ac.route("/")
def index():
    return render_template("index.html")

@ac.route("/signup",methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        account = Account(
            account_name = form.accountname.data,
            email = form.email.data,
            password = form.password.data,
            permission_id = 1
        )
        # メールアドレスの重複チェック
        if account.is_duplicate_email():
            flash("指定のメールアドレスは登録済みです")
            return redirect(url_for("accounts.signup"))
        db.session.add(account)
        db.session.commit()
        login_user(account)
        # リダイレクト先をhousebooks.indexにする
        next_ = request.args.get("housebooks.index")
        if next_ is None or not next_.startswith("/"):
            next_=url_for("housebooks.read")
        return redirect(next_)
    return render_template("signup.html",form=form)

@ac.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    # 送信されたら起動
    if form.validate_on_submit():
        account=Account.query.filter_by(email=form.email.data).first()
        # ログイン情報が正しいか判断
        if account is not None and account.verify_password(form.password.data):
            login_user(account)
            return redirect(url_for("housebooks.read"))
        
        flash("メールアドレスかパスワードが不正です")
    return render_template("login.html",form=form)

@ac.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("accounts.login"))