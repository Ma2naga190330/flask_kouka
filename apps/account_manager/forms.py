from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(FlaskForm):
    accountname = StringField(
        "アカウント名",
        validators=[
            DataRequired("ユーザ名は必須です")
        ]
    )
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired("メールアドレスは入力必須です"),
            Email("メールアドレスの形式で入力して下さい")
        ]
    )
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired("パスワードは入力必須です")
        ]
    )
    submit = SubmitField("新規登録")

# ログイン用のフォーム
class LoginForm(FlaskForm):
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired("メールアドレスは必須です。"),
            Email("メールアドレスの形式で入力してください"),
        ],
    )
    password = PasswordField(
        "パスワード",
        validators=[DataRequired("パスワードは必須です。")]
        )
    submit = SubmitField("ログイン")