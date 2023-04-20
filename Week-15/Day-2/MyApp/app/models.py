from app import db
from datetime import datetime

countries_films = db.Table('countries_films',
                           db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
                           db.Column('films_id', db.Integer, db.ForeignKey('film.id'))

)

categories_films = db.Table('categories_films',
                           db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
                           db.Column('films_id', db.Integer, db.ForeignKey('film.id'))

)

directors_films = db.Table('directors_films',
                           db.Column('director_id', db.Integer, db.ForeignKey('director.id')),
                           db.Column('films_id', db.Integer, db.ForeignKey('film.id'))

)


class Country(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(64), unique=True, nullable=False)
    films_produced = db.relationship('Film', backref='country', lazy=True)

    def save_country(self):
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def save_category(self):
        db.session.add(self)
        db.session.commit()

class Film(db.Model):
    id                 = db.Column(db.Integer, primary_key=True)
    title              = db.Column(db.String(64), unique=True, nullable=False)
    release_date       = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_in_country = db.Column(db.Integer, db.ForeignKey('country.id'))
    available_in_countries = db.relationship('Country', secondary=countries_films, backref='films_available')
    category               = db.relationship('Category', secondary=categories_films, backref='films')
    director               = db.relationship('Director', secondary=directors_films, backref='films')

    def save_film(self):
        db.session.add(self)
        db.session.commit()

class Director(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name  = db.Column(db.String(64), nullable=False)
    
    def save_director(self):
        db.session.add(self)
        db.session.commit()


