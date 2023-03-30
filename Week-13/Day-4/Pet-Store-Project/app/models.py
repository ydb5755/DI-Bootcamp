from app import db
import datetime




class Cart(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    pets = db.relationship('Pet', backref='cart', lazy='dynamic') 

    def add_to_cart(self, pet_id):
        pet = Pet.query.filter_by(id=pet_id).first()
        self.pets.append(pet)
        db.session.commit()

    def remove_from_cart(self, pet_id):
        pet = Pet.query.filter_by(id=pet_id).first()
        self.pets.remove(pet)
        db.session.commit()
    
    def get_total(self):
        total = 0
        for pet in self.pets:
            total += pet.price
        return total
    



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
