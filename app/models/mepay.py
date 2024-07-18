from app import db

class Mepay(db.Model):
    __tablename__= 'mepay'
    id = db.Column(db.Integer, primary_key=True)
    orders = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    customers = db.Column(db.Integer, db.ForeignKey('costumers.id'), primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)