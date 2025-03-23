#!/usr/bin/python3
"""Flask application with SQLite database support."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def create_database():
    """Create and populate the SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

def read_json_data():
    """Read data from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Read data from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

def read_sql_data(product_id=None):
    """Read data from SQLite database."""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
            
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    """Route to display products from various sources."""
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Initialize variables
    products_data = []
    error_message = None
    
    # Get data based on source
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    elif source == 'sql':
        try:
            if product_id:
                product_id = int(product_id)
            products_data = read_sql_data(product_id)
        except ValueError:
            error_message = "Invalid product ID"
    else:
        error_message = "Wrong source"
    
    # Check if product was found when ID was provided
    if product_id and not error_message and not products_data:
        error_message = "Product not found"
    
    return render_template('product_display.html',
                         products=products_data,
                         error_message=error_message)

if __name__ == '__main__':
    create_database()  # Create and populate the database
    app.run(debug=True, port=5000) 