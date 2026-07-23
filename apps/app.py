from flask import Flask
from apps.config import config
# db
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# csrf
from flask_wtf.csrf import CSRFProtect
# ログイン
from flask_login import LoginManager

# db
db = SQLAlchemy()
csrf = CSRFProtect()

# login
login_manager = LoginManager()
login_manager.login_view ="accounts.signup"
login_manager.login_message=""

def create_app(config_key):
    app=Flask(__name__)
    app.config.from_object(config[config_key])
    csrf.init_app(app)
    db.init_app(app)
    Migrate(app,db)
    login_manager.init_app(app)

    from apps.account_manager import views as ac_view
    app.register_blueprint(ac_view.ac,url_prefix="/")
    from apps.housebooks import views as hb_view
    app.register_blueprint(hb_view.hb,url_prefix="/housebooks")
    from apps.category_sort import views as cs_view
    app.register_blueprint(cs_view.cs,url_prefix="/categories")
    return app