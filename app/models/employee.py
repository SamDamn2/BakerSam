from app import db

class Employee(db.Model):
    __tablename__= 'employee'
    id = db.Column(db.Integer, primary_key=True)
    nombremp = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    cedula = db.Column(db.Integer, nullable=False)