from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(personal_idpersonal):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.personal import Personal
        return Personal.query.get(int(personal_idpersonal))

    from app.routes import carritoRoutes, facturaRoutes, productoRoutes, clienteRoutes, categoriaRoutes, proveedorRoutes, baseRoutes
    app.register_blueprint(productoRoutes.bp)
    app.register_blueprint(baseRoutes.bp)
    app.register_blueprint(categoriaRoutes.bp)
    app.register_blueprint(proveedorRoutes.bp)
    app.register_blueprint(facturaRoutes.bp)
    app.register_blueprint(carritoRoutes.bp)
    app.register_blueprint(clienteRoutes.bp) 

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app