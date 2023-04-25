from app import db
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text



class Thread(db.Model):
    id = Column(Integer, primary_key=True)
    subject = Column(db.String(64), nullable=False)
    comments = db.relationship('Comment', backref='thread_parent', lazy='dynamic')
    poster = Column(Integer, ForeignKey('user.id'))

    def save_thread(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    thread_parent = Column(Integer, ForeignKey('thread.id'))
    commenter = Column(Integer, ForeignKey('user.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
