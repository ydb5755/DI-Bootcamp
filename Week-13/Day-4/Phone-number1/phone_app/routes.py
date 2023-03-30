from phone_app import app, models
from flask import render_template



@app.route('/person/<phone_number>')
def by_number(phone_number):
    if models.Phone_Number.query.filter_by(number=phone_number).first():
        list_of = models.Phone_Number.query.filter_by(number=phone_number).first().owner
        user = models.Person.query.filter_by(id=list_of).first()
        return render_template('number.html', user=user)
    else:
        return 'No results found'

@app.route('/name/<name>')
def by_name(name):
    if models.Person.query.filter_by(name=name).first():
        user = models.Person.query.filter_by(name=name).first()
        return render_template('name.html', user=user)
    else:
        return 'No results found'