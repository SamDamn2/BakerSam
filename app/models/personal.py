from flask_login import UserMixin
from app import db

class Personal(db.Model, UserMixin):
    __tablename__ = 'personal'
    idpersonal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreperso = db.Column(db.String(255), nullable=False)
    tipoperso = db.Column(db.String(255), nullable=False)
    cargoperso = db.Column(db.String(255), nullable=False)
    cedulaperso = db.Column(db.BigInteger, nullable=False)
    passwordperso = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.idpersonal)