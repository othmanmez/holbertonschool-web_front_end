#!/usr/bin/python3
"""Basic Flask application with Jinja templates."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Route for home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Route for about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Route for contact page."""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 