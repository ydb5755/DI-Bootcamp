from random import choice
from string import ascii_letters

key = ''
for i in range(256):
    key += choice(ascii_letters)

class Config:
    SECRET_KEY = key