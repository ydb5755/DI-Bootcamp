import os



class Config():
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'star.db')
    SECRET_KEY = os.environ.get('SECRET_KEY')