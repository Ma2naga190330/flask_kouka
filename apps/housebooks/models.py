from apps.app import db
from datetime import datetime
from sqlalchemy.orm import relationship

# カテゴリテーブル
class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(), nullable=False)
    moneybooks = db.relationship('MoneyBooks', backref='category', lazy=True)


# 家計簿テーブル
class MoneyBooks(db.Model):
    __tablename__ = "moneybooks"

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    comment = db.Column(db.String)
    price = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = db.Column(db.Boolean, default=False)