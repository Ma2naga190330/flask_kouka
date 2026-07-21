from pathlib import Path

basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = "aaaaaaaaaaaaaaa"
    WTF_CSTF_SECRET_KEY = "aaaaaaaaaaa"

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