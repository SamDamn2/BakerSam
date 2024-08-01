from app import db

class Metodopago(db.Model):
    __tablename__ = 'metodopago'
    idmetodopago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    metodo = db.Column(db.String(50), nullable=False)  # Ej. 'Tarjeta de Crédito', 'Efectivo'

    facturas = db.relationship('Factura', back_populates='metodopago')
