from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Email,Length

class MoneyBookForm(FlaskForm):
    account_id = IntegerField(
        "アカウントid",
        validators=[
            DataRequired(message="アカウントidは必須です")
        ]
    )

    comment = StringField(
        "カテゴリー",
        validators=[
            DataRequired(message="カテゴリーは必須です")
        ]
    )

    price = IntegerField(
        "金額",
        validators=[
            DataRequired(message="金額は必須です")
        ]
    )

    submit = SubmitField("新規登録")

# csrf回避のため
class DeleteForm(FlaskForm):
    pass
class UpdateForm(FlaskForm):
    pass