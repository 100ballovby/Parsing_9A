from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'try-to-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # указываю путь к БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *
from models import *

if __name__ == '__main__':
    app.run(port=4893, debug=True)
