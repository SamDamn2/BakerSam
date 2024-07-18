from app import db

class Order(db.Model):
    __tablename__= 'order'
    id = db.Column(db.Integer, primary_key=True)
    employees = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    customers = db.Column(db.Integer, db.ForeignKey('costumer.id'), primary_key=True)
    fecha = db.Column(db.DATE, nullable=False)
    preciototal = db.Column(db.String(255), nullable=False)