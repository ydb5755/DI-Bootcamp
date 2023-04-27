from app import db
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text
from app.forum.forms import CommentForm


class Thread(db.Model):
    id = Column(Integer, primary_key=True)
    subject = Column(db.String(64), nullable=False)
    comments = db.relationship('Comment', backref='thread', lazy='dynamic')
    poster = Column(Integer, ForeignKey('user.id'))

    def save_thread(self):
        db.session.add(self)
        db.session.commit()

    def comment_on_thread(self):
        form = CommentForm()
        form.parent_thread.data = self.id
        return form

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    thread_parent = Column(Integer, ForeignKey('thread.id'))
    commenter = Column(Integer, ForeignKey('user.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
