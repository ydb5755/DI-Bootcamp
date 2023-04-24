from app import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)