import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SECRET_KEY']='123456'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from phone_app import models, routes

fake = Faker()



# with app.app_context():
    # thing = models.Phone_Number.query.all()
    # print(thing[0].owner.name)


    # user = models.Person(name=fake.name(), email=fake.email(), address=fake.address() )
    # db.session.add(user)
    # db.session.commit()
    
    # num = models.Phone_Number(number=fake.phone_number(), person=user)
    # db.session.add(num)
    # db.session.commit()
    # print(num.owner.name)

    # for _ in range(10):
    #     user = models.Person(name=fake.name(), email=fake.email(), address=fake.address() )
    #     db.session.add(user)
    # db.session.commit()
    # people = models.Person.query.all()
    # for person in people:
    #     num = models.Phone_Number(number=fake.phone_number(), person=person)
    #     db.session.add(num)
    # db.session.commit()


