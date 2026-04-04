#!/usr/bin/python3
"""
Flask app that displays products from JSON, CSV, or SQLite
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_json_data():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None

def get_csv_data():
    try:
        data = []
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                data.append(row)
        return data
    except Exception:
        return None

def get_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return data

    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'json':
        products = get_json_data()
    elif source == 'csv':
        products = get_csv_data()
    elif source == 'sql':
        products = get_sql_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    if products is None:
        return render_template('product_display.html', error="Error loading data")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(port=5000)
