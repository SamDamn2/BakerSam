from app import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    idcategoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipocga = db.Column(db.String(255), nullable=False)

    productos = db.relationship('Producto', back_populates='categoria')
