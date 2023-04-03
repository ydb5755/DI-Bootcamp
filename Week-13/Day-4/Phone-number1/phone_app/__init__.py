import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from random import randint

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SECRET_KEY']='123456'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from phone_app import routes
from phone_app.models import Person, Nationalities, Phone_Number

fake = Faker()



# with app.app_context():
    # america = Nationalities(name='america')
    # russia = Nationalities(name='russia')
    # norway = Nationalities(name='norway')
    # db.session.add_all([norway,russia, america])
    # db.session.commit()


    # for _ in range(10):
    #     user = Person(name=fake.name(), email=fake.email(), address=fake.address() )
    #     db.session.add(user)
    # db.session.commit()
    # people = Person.query.all()
    # print(people[2].phone_numbers.first().number)
    # for person in people:
    #     num = Phone_Number(number=fake.phone_number(), person=person)
    #     db.session.add(num)


    # nation = Nationalities.query.all()
    # people = Person.query.all()
    # number_of_people = len(people)
    # number_of_nationalities = len(nation)
    # for nation in people[2].nationalities:
    #     print(nation.name)


    # for _ in range(number_of_people):
    #     people[randint(0, number_of_people-1)].nationalities.append(nation[randint(0, number_of_nationalities-1)])
    # db.session.commit()


