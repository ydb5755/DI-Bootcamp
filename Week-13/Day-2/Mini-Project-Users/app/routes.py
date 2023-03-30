from app import app, db
from app.models import User
from flask import render_template, request, redirect, url_for, flash, abort
from app.forms import UserForm, LoginForm
import json
import requests
from flask_login import login_user, logout_user, current_user, login_required

# @app.route('/', methods=("GET", "POST"))
# def home():
#     form = UserForm()
#     if form.validate_on_submit():
#         data = request.get_json()
#         return render_template('home.html', data=data, form=form)
#     return render_template('home.html', form=form)

def open_json_file(file_path):
    with open(file_path) as f:
        return json.load(f)

def zipcode_func():
    result = []
    all = User.query.all()
    for person in all:
        new_list = [i for i in person.zipcode]
        if int(new_list[0]) == 5:
            result.append(person)
    return result

@app.route('/')
def index():
    my_file = User.query.all()
    first_five = User.query.limit(5)
    zipcode_5 = zipcode_func()
    return render_template('index.html', my_file=my_file, first_five=first_five, zipcode_5=zipcode_5)

@app.route('/add_user', methods=("GET", "POST"))
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, street=form.street.data, city=form.city.data, zipcode=form.zipcode.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    # if current_user.is_authenticated:
    #     redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user.city == form.city.data:
            login_user(user)
            flash('You have logged in!') 
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('No user matches these credentials')
            return redirect(url_for('add_user'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @app.route('/populate')
# def populate():
#     jfile = open_json_file('C:/Users/Lenovo/Desktop/DI_Bootcamp/Week-13/Day-2/Mini-Project-Users/users.json')
#     for person in jfile:
#         user = User(name=person.get('name'), street=person.get('address').get('street'), city=person.get('address').get('city'), zipcode=person.get('address').get('zipcode'))
#         db.session.add(user)
#     db.session.commit()

#     return render_template('index.html')