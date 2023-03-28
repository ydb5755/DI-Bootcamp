from app import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(64))
    street   = db.Column(db.String(64))
    city     = db.Column(db.String(64))
    zipcode  = db.Column(db.String(64))

    def __repr__(self):
        return f'User (id-{self.id}, name-{self.name}, street-{self.street}, city-{self.city}, zipcode-{self.zipcode})'