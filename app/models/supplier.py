from app import db

class Supplier(db.Model):
    __tablename__= 'supplier'
    id = db.Column(db.Integer, primary_key=True)
    nombrepve = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)