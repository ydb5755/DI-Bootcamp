from to_do import db

class Todo(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    details   = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean)
    image     = db.relationship('Image', backref='todo', uselist=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def set_task_as_complete(self):
        Todo.query.filter_by(id=self.id).first().completed = True
        db.session.commit()
        
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()