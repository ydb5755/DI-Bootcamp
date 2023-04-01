from to_do import db

class Todo(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def set_task_as_complete(self):
        Todo.query.filter_by(id=self.id).first().completed = True
        db.session.commit()
        