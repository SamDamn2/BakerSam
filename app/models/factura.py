from datetime import datetime
from app import db

class Factura(db.Model):
    __tablename__ = 'factura'
    idfactura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fechafta = db.Column(db.DateTime, default=datetime.utcnow)
    idcliente = db.Column(db.Integer, db.ForeignKey('cliente.idcliente'))

    cliente = db.relationship("Cliente", back_populates="facturas")
    productos = db.relationship("Detallefactura", back_populates="factura")

    idmetodopago = db.Column(db.Integer, db.ForeignKey('metodopago.idmetodopago'))
    metodopago = db.relationship('Metodopago', back_populates='facturas')