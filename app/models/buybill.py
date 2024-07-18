from app import db

class Buybill(db.Model):
    __tablename__= 'buybill'
    id = db.Column(db.Integer, primary_key=True)
    buys = db.Column(db.Integer, db.ForeignKey('buy.id'), primary_key=True)
    products = db.Column(db.String(255), db.ForeignKey('product.id'), primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    preciouni = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)