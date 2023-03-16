import json



def retrieve_all_products():
    with open('Week-11\Day-5\products.json') as f:
        all_products = json.load(f)
        return all_products

def retrieve_requested_product(product_id):
    items = retrieve_all_products()
    for item in items:
        if item['ProductId'] == product_id:
            return item
    return None
