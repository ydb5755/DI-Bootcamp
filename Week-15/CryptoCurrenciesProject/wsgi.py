from app import crypto_data_call #, create_app
from app.models import Crypto
from app import db, app

# app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # data = crypto_data_call()
        # for coin in data:
        #     c = Crypto(id=coin['id'],
        #                name=coin['name'],
        #                symbol=coin['symbol'],
        #                slug=coin['slug'],
        #                first_historical_data=coin['first_historical_data'],
        #                last_historical_data=coin['last_historical_data'],
        #                is_active=coin['is_active']
        #                )
        #     db.session.add(c)
        # db.session.commit()
        app.run(debug=True)










# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json

# url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)