from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from app.profiles.models import Card
from app import db
import random

def swapi_people_call(num):
    url = 'https://swapi.dev/api/people/' 

    session = Session()
    try:
        response = session.get(url + f'{num}')
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e

def swapi_planets_call(num):
    url = 'https://swapi.dev/api/planets/' # you created a global var called url which is great so use it by change it to 'https://swapi.dev/api' and update all the places

    session = Session()
    try:
        response = session.get(url + f'{num}')
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e

def swapi_vehicles_call(num):
    url = 'https://swapi.dev/api/vehicles/'

    session = Session()
    try:
        response = session.get(url + f'{num}')
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e

def swapi_starships_call(num):
    url = 'https://swapi.dev/api/starships/'

    session = Session()
    try:
        response = session.get(url + f'{num}')
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
    

def create_people_cards():
    for x in range(swapi_people_call('/')['count']): #type: ignore
        person = swapi_people_call(x + 1)
        try:
            if person['name'] == None:       #type: ignore
                continue
            card = Card(
                name=person['name'],       #type: ignore
                point_value=random.randint(1,10), 
                details={
                    'Height':person['height'],       #type: ignore
                    'Mass':person['mass'],       #type: ignore
                    'Hair_Color':person['hair_color'],       #type: ignore
                    'Skin_Color':person['skin_color'],       #type: ignore
                    'Eye_Color':person['eye_color'],       #type: ignore
                    'Gender':person['gender']       #type: ignore
                }
            )
            db.session.add(card)
        except:
            continue
    db.session.commit()

def create_planets_cards():
    for x in range(swapi_planets_call('/')['count']): #type: ignore
        planet = swapi_planets_call(x + 1)
        try: # why you put this in try and except? inorder to check if the planet contains name key you can do the following: planet.get('name', None) == None
            if planet['name'] == None:  #type: ignore
                continue
            card = Card(
                name=planet['name'],#type: ignore
                point_value=random.randint(1,10), 
                details={
                    'diameter':planet['diameter'],#type: ignore
                    'climate':planet['climate'],#type: ignore
                    'gravity':planet['gravity'],#type: ignore
                    'terrain':planet['terrain'],#type: ignore
                    'surface_water':planet['surface_water'],#type: ignore
                    'population':planet['population']#type: ignore
                }
            )
        except:
            continue
        db.session.add(card)
    db.session.commit()

def create_vehicles_cards():
    for x in range(swapi_vehicles_call('/')['count']): #type: ignore
        vehicle = swapi_vehicles_call(x + 1)
        try:
            if vehicle['name'] == None:  #type: ignore
                continue
            card = Card(
                name=vehicle['name'],#type: ignore
                point_value=random.randint(1,10), 
                details={
                    'model':vehicle['model'],#type: ignore
                    'manufacturer':vehicle['manufacturer'],#type: ignore
                    'max_atmosphering_speed':vehicle['max_atmosphering_speed'],#type: ignore
                    'passengers':vehicle['passengers'],#type: ignore
                    'crew':vehicle['crew'],#type: ignore
                    'cargo_capacity':vehicle['cargo_capacity']#type: ignore
                }
            )
        except:
            continue
        db.session.add(card)
    db.session.commit()



def create_starships_cards():
    for x in range(swapi_starships_call('/')['count']): #type: ignore
        starship = swapi_starships_call(x + 1)
        try:
            if starship['name'] == None:  #type: ignore
                continue
            card = Card(
                name=starship['name'],#type: ignore
                point_value=random.randint(1,10),
                details={
                    'model':starship['model'],#type: ignore
                    'manufacturer':starship['manufacturer'],#type: ignore
                    'max_atmosphering_speed':starship['max_atmosphering_speed'],#type: ignore
                    'passengers':starship['passengers'],#type: ignore
                    'hyperdrive_rating':starship['hyperdrive_rating'],#type: ignore
                    'starship_class':starship['starship_class']#type: ignore
                }
            )
        except:
            continue
        db.session.add(card)
    db.session.commit()
