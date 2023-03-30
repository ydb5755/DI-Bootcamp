from app import app 
from flask import render_template, redirect, url_for
from app.models import Pet, Cart

def get_all_pets():
    return Pet.query.all()

def get_one_pet(id):
    return Pet.query.filter_by(id=id).first()

def get_customer_cart():
    return Cart.query.filter_by(name='Customer Cart').first()

@app.route('/')
def index():
    pic1 = get_all_pets()[0].image
    pic2 = get_all_pets()[1].image
    return render_template('index.html', pic1=pic1, pic2=pic2)

@app.route('/pets')
def pets():
    return render_template('pets.html', all_pets=get_all_pets())

@app.route('/pet/<int:pet_id>')
def individual_pet(pet_id):
    pet = get_one_pet(pet_id)
    return render_template('pet.html', pet=pet)

@app.route('/cart')
def cart():
    c = get_customer_cart()
    return render_template('cart.html', c=c)

@app.route('/add_pet/<int:pet_id>')
def add_pet(pet_id):
    customer_cart = get_customer_cart()
    customer_cart.add_to_cart(pet_id)
    return redirect(url_for('pets'))

@app.route('/remove_pet/<int:pet_id>')
def remove_pet(pet_id):
    customer_cart = get_customer_cart()
    customer_cart.remove_from_cart(pet_id)
    return redirect(url_for('cart'))

@app.route('/contact')
def contact():
    return render_template('contact.html')