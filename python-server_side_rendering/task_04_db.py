from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sqlite(db_file):
    products = []
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error:
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
    elif source == 'sql':
        products = read_sqlite('products.db')
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
