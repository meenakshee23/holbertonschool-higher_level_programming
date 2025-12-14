from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products

@app.route('/products')
def show_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            products = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
