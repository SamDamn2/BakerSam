from app import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    idcliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrecte = db.Column(db.String(255), nullable=False)
    direccioncte = db.Column(db.String(255), nullable=False)
    telefonocte = db.Column(db.BigInteger, nullable=False)

    facturas = db.relationship("Factura", back_populates="cliente")