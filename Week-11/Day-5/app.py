from products_data import retrieve_all_products, retrieve_requested_product
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/products')
def products():
    return render_template('products.html', data=retrieve_all_products())

@app.route('/products/<product_id>')
def product_details(product_id):
    return render_template('product_details.html', product_id=retrieve_requested_product(product_id), data=retrieve_all_products())

app.run(debug=True)