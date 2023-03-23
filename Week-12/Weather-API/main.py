import datetime as dt
import requests
import secrets

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = 'e5261eb2d930a8763ba27db14330ce03'
CITY = "Jerusalem"


def kelvin_to_celsius_and_farenheight(kelvin):
    celsius = kelvin - 273.15
    farenheight = celsius * (9/5) + 32
    return celsius, farenheight

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_farenheight = kelvin_to_celsius_and_farenheight(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farenheight = kelvin_to_celsius_and_farenheight(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# print(f'Temperature in {CITY}: {temp_celsius:.2f} C or {temp_farenheight:.2f} F')
# print(f'Temperature in {CITY} feels like: {feels_like_celsius:.2f} C or {feels_like_farenheight:.2f} F')
# print(f'Humidity in {CITY}: {humidity}%')
# print(f'Wind Speed in {CITY}: {wind_speed} m/s')
# print(f'General Weather in {CITY}: {description}')
# print(f'Sun rises in {CITY}: {sunrise_time} local time')
# print(f'Sun sets in {CITY}: {sunset_time} local time')
# print(response['main'])

