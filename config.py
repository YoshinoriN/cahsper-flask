import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('CAHSPER_DB_URL', 'mysql+pymysql://{user}:{password}@127.0.0.1/cahsper').format(**{
        'user': os.getenv('CAHSPER_DB_USER', 'root'),
        'password': os.getenv('CAHSPER_DB_PASSWORD', 'pass')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
