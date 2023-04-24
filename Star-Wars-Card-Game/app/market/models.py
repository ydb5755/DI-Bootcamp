from app import db
from sqlalchemy import Column, String, Integer, Boolean


class Trade(db.Model):
    id = Column(Integer, primary_key=True)
    card1 = Column(String(64), nullable=False)
    card2 = Column(String(64), nullable=False)
    accepted = Column(Boolean)

class Sale(db.Model):
    id = Column(Integer, primary_key=True)
    card = Column(String(64), nullable=False)
    coins = Column(Integer, nullable=False)
    accepted = Column(Boolean)
