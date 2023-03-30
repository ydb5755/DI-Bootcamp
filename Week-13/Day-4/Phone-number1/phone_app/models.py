from phone_app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    phone_numbers = db.relationship('Phone_Number', backref='person', lazy='dynamic')
    address = db.Column(db.String(200))

class Phone_Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))