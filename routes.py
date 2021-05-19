from flask import render_template, redirect, url_for
from app import app, db
from models import Pizzas


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/update')
def update():
    return redirect(url_for('main_page'))