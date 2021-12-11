import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    POSTS_PER_PAGE = 10

class Dev(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    PROPAGATE_EXCEPTIONS = True

class Test(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
