from app import db
import datetime




class Pet(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(64), unique=True)
    gender        = db.Column(db.String(1)) #validate for M/F
    breed         = db.Column(db.String(64))
    date_of_birth = db.Column(db.DateTime, default=datetime.date.today())
    details       = db.Column(db.Text)
    price         = db.Column(db.Integer)
    image         = db.Column(db.String(200))
    cart_id       = db.Column(db.Integer, db.ForeignKey('cart.id'))

class Cart(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    pets = db.relationship('Pet', backref='pet_cart')