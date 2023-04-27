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
    coins        = Column(Integer, default=50)
    cards        = db.relationship('Card', backref='current_owner', lazy='dynamic')
    threads      = db.relationship('Thread', backref='user', lazy='dynamic') 
    comments     = db.relationship('Comment', backref='user', lazy='dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    def get_card_points(self):
        total = 0
        for card in self.cards:
            total += card.point_value
        return total

class Card(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(db.String(64), nullable=False)
    on_market = Column(Boolean, default=False)
    point_value = Column(Integer, nullable=False)
    details = Column(Text)
    set_price = Column(Integer)
    owner = Column(Integer, ForeignKey('user.id'))

