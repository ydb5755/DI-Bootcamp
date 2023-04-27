from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def swapi_data_call(cat, num, attr):
    url = 'https://swapi.dev/api/'

    session = Session()
    try:
        response = session.get(url + f'{cat}/{num}/')
        data = json.loads(response.text)
        return data[attr]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
    

def swapi_main_call():
    url = 'https://swapi.dev/api/'

    session = Session()
    try:
        response = session.get(url)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
    
def swapi_cat_call(cat):
    url = 'https://swapi.dev/api/'

    session = Session()
    try:
        response = session.get(url + f'{cat}')
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
categories = ['people', 'planets', 'vehicles', 'starships']


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
    url = 'https://swapi.dev/api/planets/'

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
        try:
            print(swapi_people_call(x + 1)['name'])  #type: ignore
        except:
            continue

def create_planets_cards():
    for x in range(swapi_planets_call('/')['count']): #type: ignore
        print(swapi_planets_call(x + 1))

def create_vehicles_cards():
    for x in range(swapi_vehicles_call('/')['count']): #type: ignore
        try:
            print(swapi_vehicles_call(x + 1)['name']) #type: ignore
        except:
            continue


def create_starships_cards():
    for x in range(swapi_starships_call('/')['count']): #type: ignore
        try:
            print(swapi_starships_call(x + 1)) #type: ignore
        except:
            continue

def swapi():
    url = 'https://swapi.dev/api/planets/'

    session = Session()
    try:
        response = session.get(url)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e


print(create_vehicles_cards())

# def sw():
#     url = 'https://swapi.dev/api/vehicles/'

#     session = Session()
#     try:
#         response = session.get(url)
#         data = json.loads(response.text)
#         return data
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         return e

# print(sw())