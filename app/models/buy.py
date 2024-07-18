from app import db

class Buy(db.Model):
    __tablename__= 'buy'
    id = db.Column(db.Integer, primary_key=True)
    suppliers = db.Column(db.Integer, db.ForeignKey('supplier.id'), primary_key=True)
    nombreprod = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precioto = db.Column(db.Float, nullable=False)