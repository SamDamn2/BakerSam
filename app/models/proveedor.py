from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    idproveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrepvr = db.Column(db.String(255), nullable=False)
    cedulapvr = db.Column(db.String(20), nullable=False)
    telefonopvr = db.Column(db.String(20), nullable=False)
    
    productos = db.relationship('Producto', back_populates='proveedor')
