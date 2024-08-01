from app import db

class Detallefactura(db.Model):
   __tablename__ = 'detallefactura'
   iddetalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
   idfactura = db.Column(db.Integer, db.ForeignKey('factura.idfactura'))
   idproducto = db.Column(db.Integer, db.ForeignKey('producto.idproducto'))
   cantidad = db.Column(db.Integer, nullable=False)
    
   factura = db.relationship("Factura", back_populates="productos")
   producto = db.relationship("Producto", back_populates="detalle_facturas")
