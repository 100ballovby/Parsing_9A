from app import db


class Pizzas(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    original_link = db.Column(db.String(200))
    name = db.Column(db.String(120), index=True)
    ingredient = db.Column(db.String(255))
    price = db.Column(db.String(50))
    img_link = db.Column(db.String(200))

