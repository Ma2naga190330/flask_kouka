from pathlib import Path

basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = "aaaaaaaaaaaaaaa"
    WTF_CSTF_SECRET_KEY = "aaaaaaaaaaa"
    # 判定したいカテゴリリスト
    CATEGORIES = [
        "食費",
        "日用品",
        "交通費",
        "娯楽・趣味",
        "光熱費・通信費"
    ]

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

class TestingConfig(BaseConfig):
    pass

config = {
    "testting":TestingConfig,
    "local":LocalConfig,
}