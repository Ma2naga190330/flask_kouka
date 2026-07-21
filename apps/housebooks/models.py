from apps.app import db
from datetime import datetime

class MoneyBooks(db.Model):
    __tablename__ = "moneybooks"

    id = db.Column(db.Integer,primary_key=True)
    account_id = db.Column(db.Integer)
    comment = db.Column(db.String)
    price = db.Column(db.Integer)
    create_at = db.Column(db.DateTime,default=datetime.now)
    update_at = db.Column(db.DateTime,default=datetime.now,onupdate=datetime.now)