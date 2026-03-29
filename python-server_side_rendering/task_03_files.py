from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv_file(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    else:
        error = "Wrong source"
        data = []

    if product_id is not None and not error:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
