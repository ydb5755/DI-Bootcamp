import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SECRET_KEY']='123456'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)
# login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import models, routes


# user = models.User(id=0, name='Yisroel Baum', street='NY ave', city='Brooklyn', zipcode=11210)
# db.session.add(user)
# db.session.commit()

