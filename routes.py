from flask import render_template, redirect, url_for
from app import app, db
from models import Pizzas


@app.route('/index')
def main_page():
    return render_template('index.html')
