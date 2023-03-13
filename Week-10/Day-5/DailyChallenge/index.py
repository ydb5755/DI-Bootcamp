# Instructions :
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.


import requests
import time
def request_time(url):
    x = time.time()
    requests.get(url)
    y = time.time()
    return f'The response time for this website was {y-x} seconds'

print(request_time('https://facebook.com'))