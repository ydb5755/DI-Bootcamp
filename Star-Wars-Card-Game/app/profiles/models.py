from app import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text


class User(db.Model, UserMixin):
    id           = Column(Integer, primary_key=True)
    first_name   = Column(db.String(64), nullable=False)
    last_name    = Column(db.String(64), nullable=False)
    profile_type = Column(db.String(64), nullable=False)
    username     = Column(db.String(64), nullable=False, unique=True)
    email        = Column(db.String(64), nullable=False, unique=True)
    password     = Column(db.String(64), nullable=False)
    coins        = Column(Integer)
    cards        = db.relationship('Card', backref='current_owner', lazy='dynamic')
    threads      = db.relationship('Thread', backref='poster', lazy='dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Card(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(db.String(64), nullable=False)
    on_market = Column(Boolean, default=False)
    point_value = Column(Integer, nullable=False)
    details = Column(Text)
    owner = Column(Integer, ForeignKey('user.id'))

class Thread(db.Model):
    id = Column(Integer, primary_key=True)
    subject = Column(db.String(64), nullable=False)
    comments = db.relationship('Comment', backref='thread_relation', lazy='dynamic')
    poster = Column(Integer, ForeignKey('user.id'))

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
