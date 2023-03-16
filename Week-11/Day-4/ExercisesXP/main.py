# Look at the pictures at the bottom of the page, to understand the assignment



# Instructions :
# Note: For this exercise, we will use the JSON file provided in the assets below.

# This database contains a list of dictionaries. Each dictionary contains these keys:

# ProductId, Category, MainCategory,TaxTarifCode, SupplierName, WeightMeasure
# WeightUnit, Description, Name, ProductPicUrl, Status, Quantity, UoM, CurrencyCode
# Price, Width, Depth, Height, DimUnit
# We will be using these keys to represent each item in our marketplace.
# You don’t have to use all the keys.

# Build a marketplace website, the website should have 3 pages:
# A homepage, with a welcome message, routed to /.
# A products page, that displays a list of all the products that are for sale, routed to /products.
# A product details page, that displays the details of the selected product (the product id should be passed into the URL), routed to /product/<product_id>
import flask
import json

app = flask.Flask(__name__)


def data_load():
    with open('Week-11\Day-4\ExercisesXP\product_db.json') as f:
        data = json.load(f)
    return data

@app.route('/')
def homepage():
    return flask.render_template('homepage.html')

@app.route('/products')
def products():
    return flask.render_template('products.html', data=data_load())

@app.route('/product/<product_id>')
def product_details(product_id):
    return flask.render_template('product-details.html', product_id=product_id, data=data_load())

app.run(debug=True)