from products_data import retrieve_all_products, retrieve_requested_product
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/products')
def products():
    return render_template('products.html', 
                           data=retrieve_all_products())

@app.route('/products/<product_id>')
def product_details(product_id):
    return render_template('product_details.html', 
                           product_id=retrieve_requested_product(product_id))

@app.route('/cart')
def cart_page():
    return render_template('cart.html', 
                           data=retrieve_all_products(), 
                           cart_item=cart_item,
                           total=total_cost())

@app.route('/add_product_to_cart/<product_id>')
def add_product(product_id):
    add_func(retrieve_requested_product(product_id))
    return redirect(url_for('products'))

@app.route('/remove_product_from_cart/<product_id>')
def remove_product(product_id):
    remove_func(retrieve_requested_product(product_id))
    return redirect(url_for('cart_page'))

cart_item = []
def total_cost():
    total = 0
    for item in cart_item:
        total += item['Price']
    return total

def add_func(product_id):
    cart_item.append(product_id)

def remove_func(product_id):
    cart_item.remove(product_id)

app.run(debug=True)