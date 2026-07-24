from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired

class MoneyBookForm(FlaskForm):
    account_id = IntegerField(
        "アカウントid",
        validators=[
            DataRequired(message="アカウントidは必須です")
        ]
    )

    comment = StringField(
        "内訳",
        validators=[
            DataRequired(message="内訳は必須です")
        ]
    )

    # プルダウン形式で選択
    category_id = SelectField(
        'カテゴリ',
        coerce=int,
        validators=[DataRequired(message="カテゴリを選択してください")]
    )

    price = IntegerField(
        "金額",
        validators=[
            DataRequired(message="金額は必須です")
        ]
    )

    submit = SubmitField("登録")

# csrf回避のため
class DeleteForm(FlaskForm):
    pass
class UpdateForm(FlaskForm):
    pass