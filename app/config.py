import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    DB_HOST = os.getenv('DB_HOST') or ''
    DB_PORT = os.getenv('DB_PORT') or ''
    DB_NAME = os.getenv('DB_NAME') or ''
    DB_USER = os.getenv('DB_USER') or ''
    DB_PASSWORD = os.getenv('DB_PASSWORD') or ''
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    pass


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
