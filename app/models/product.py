from app import db

class Product(db.Model):
    __tablename__= 'product'
    id = db.Column(db.Integer, primary_key=True)
    categorys = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)
    nombrepro = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)