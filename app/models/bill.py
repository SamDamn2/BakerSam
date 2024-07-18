from app import db

class Bill(db.Model):
    __tablename__= 'bill'
    id = db.Column(db.Integer, primary_key=True)
    orders = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    products = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    nombreprodu = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    preciouni = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)