import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
# db_info = {'host': 'localhost',
#            'database': 'bookstore',
#            'psw': '1234',
#            'user': 'postgres',
#            'port': ''}
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SECRET_KEY'] = '123456'


portfolio = SQLAlchemy(app)
migrate = Migrate(app, portfolio)


from portfolio import models, routes