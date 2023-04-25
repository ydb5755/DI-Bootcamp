from app import db
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text



class Thread(db.Model):
    id = Column(Integer, primary_key=True)
    subject = Column(db.String(64), nullable=False)
    comments = db.relationship('Comment', backref='thread_relation', lazy='dynamic')
    poster = Column(Integer, ForeignKey('user.id'))

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
