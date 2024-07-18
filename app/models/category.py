from app import db

class Category(db.Model):
    __tablename__= 'category'
    id = db.Column(db.Integer, primary_key=True)
    nombrecate = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Integer, nullable=False)