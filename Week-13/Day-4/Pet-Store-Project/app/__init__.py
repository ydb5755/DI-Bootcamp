import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SECRET_CODE'] = '123456'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes



with app.app_context():
    rob = models.Pet(name='Rob', gender='M', breed='Pug', details='Great doggy', price=150, image='https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=464&q=80', pet_cart=None)
    daisy = models.Pet(name='Daisy', gender='F', breed='Bijon', details='Small doggy', price=200, image='https://images.unsplash.com/photo-1583511655826-05700d52f4d9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80', pet_cart=None)
    ruby = models.Pet(name='Ruby', gender='F', breed='Tabby', details='Great kitter kat', price=25, image='https://images.unsplash.com/photo-1592194996308-7b43878e84a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80', pet_cart=None)
    chester = models.Pet(name='Chester', gender='M', breed='Dachshund', details='Baby hotdog doggy', price=450, image='https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=394&q=80', pet_cart=None)
    
    db.session.add(rob)
    db.session.add(daisy)
    db.session.add(ruby)
    db.session.add(chester)
    db.session.commit()