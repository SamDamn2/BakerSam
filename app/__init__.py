from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import carritoRoutes, facturaRoutes, productoRoutes, clienteRoutes
    app.register_blueprint(productoRoutes.bp)
    app.register_blueprint(facturaRoutes.bp)
    app.register_blueprint(carritoRoutes.bp)
    app.register_blueprint(clienteRoutes.bp) 

    return app