from app import db

class Producto(db.Model):
    __tablename__ = 'producto'
    idproducto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrepdo = db.Column(db.String(255), nullable=False)
    descripcionpdo = db.Column(db.String(255), nullable=False)
    preciopdo = db.Column(db.BigInteger, nullable=False)
    stockpdo = db.Column(db.Integer, nullable=False)
    imagenpdo = db.Column(db.String(255))
    
    detalle_facturas = db.relationship("Detallefactura", back_populates="producto")

    idcategoria = db.Column(db.Integer, db.ForeignKey('categoria.idcategoria'))
    categoria = db.relationship('Categoria', back_populates='productos')

    idproveedor = db.Column(db.Integer, db.ForeignKey('proveedor.idproveedor'))
    proveedor = db.relationship('Proveedor', back_populates='productos')