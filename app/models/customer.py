from app import db

class Customer(db.Model):
    __tablename__= 'customer'
    id = db.Column(db.Integer, primary_key=True)
    nombrecli = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(255), nullable=False)