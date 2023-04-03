from phone_app import db

person_nationality = db.Table('person_nationality',
                              db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                              db.Column('nationality_id', db.Integer, db.ForeignKey('nationalities.id'))
                              )

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    phone_numbers = db.relationship('Phone_Number', backref='person', lazy='dynamic')
    address = db.Column(db.String(200))
    nationalities = db.relationship('Nationalities', secondary=person_nationality, backref='people')


class Phone_Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))

class Nationalities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))