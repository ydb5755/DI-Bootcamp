from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SECRET_KEY']='123456'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes


# user = models.User(id=0, name='Yisroel Baum', street='NY ave', city='Brooklyn', zipcode=11210)
# db.session.add(user)
# db.session.commit()

