from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
    category_name = StringField(
        "カテゴリー名",
        validators=[
            DataRequired(message="カテゴリー名は必須です")
        ]
    )
    submit = SubmitField("送信")