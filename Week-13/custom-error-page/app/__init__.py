import os

import flask_migrate
import flask_sqlalchemy
from flask import Flask

flask_app = Flask(__name__)

db_info = {'host': 'localhost',
           'database': 'bookstore',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}

flask_app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
flask_app.config['SECRET_KEY'] = "123"

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import routes, models, error_handlers
