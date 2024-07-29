from app import db

class Order(db.Model):
    __tablename__= 'order'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DATE, nullable=False)
    preciototal = db.Column(db.String(255), nullable=False)
    products = db.relationship('Product', secondary = 'bill')