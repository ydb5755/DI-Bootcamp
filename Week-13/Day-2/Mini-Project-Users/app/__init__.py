from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'robots.db')
app.config['SECRET_KEY']='123456'

robots = SQLAlchemy(app)
migrate = Migrate(app, robots)

from app import models 

# def insert():
#     user = models.User(id=0, name='Yisroel Baum', street='NY ave', city='Brooklyn', zipcode=11210)
#     robots.session.add(user)
#     robots.session.commit()


#     id       = robots.Column(robots.Integer, primary_key=True)
#     name     = robots.Column(robots.String(64))
#     street   = robots.Column(robots.String(64))
#     city     = robots.Column(robots.String(64))
#     zipcode  = robots.Column(robots.String(64))