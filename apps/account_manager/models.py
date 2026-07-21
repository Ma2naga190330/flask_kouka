from apps.app import db,login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
# 外部キー用
from sqlalchemy.orm import relationship

# 権限設定
# class Permission():
#     __tablename__="permissions"

#     id = db.Column(db.Integer,primary_key=True)
#     class_name=db.Column(db.String)

#     accounts = relationship("Account",back_populates="permissions")
#     def __repr__(self):
#         return f"<Permissions(id={self.id}, class_name='{self.class_name}')>"

class Account(db.Model,UserMixin):
    # テーブル名
    __tablename__ = "accounts"
    # カラムの設定
    id = db.Column(db.Integer,primary_key=True)
    account_name = db.Column(db.String,index=True)
    email = db.Column(db.String,unique=True,index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime,default=datetime.now)
    updated_at = db.Column(db.DateTime,default=datetime.now,onupdate=datetime.now)
    # permission = db.Column(db.Integer,db.ForeignKey("premissions.id"))
    
    # account = relationship("Account", back_populates="accounts")

    # def __repr__(self):
    #     return f"<Account(id={self.id}, account_name='{self.account_name}', permission='{self.permission}')"
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
