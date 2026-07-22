from apps.app import db,login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
# 外部キー用
from sqlalchemy.orm import relationship

class Permission(db.Model):
    """権限マスターテーブル"""
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(50), nullable=False)

    # リレーションシップ設定
    accounts = db.relationship('Account', backref='permission', lazy=True)


class Account(db.Model):
    """アカウントテーブル"""
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)  # ハッシュ化パスワード用
    create_at = db.Column(db.DateTime, default=lambda: datetime.now())
    update_at = db.Column(db.DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())
    
    # Permissions(id) への外部キー
    permission = db.Column(db.Integer, db.ForeignKey('permissions.id'), nullable=False)

    @property
    def password(self):
        raise AttributeError("読み取り不可")
    # PWリセット
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    # PWのチェック
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    # メールアドレスの重複チェック
    def is_duplicate_email(self):
        return Account.query.filter_by(email=self.email).first() is not None
# ログイン情報を取得
@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(user_id)
