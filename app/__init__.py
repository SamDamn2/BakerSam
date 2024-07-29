from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes import billRoutes, productRoutes, orderRoutes
    app.register_blueprint(billRoutes.bp)
    app.register_blueprint(productRoutes.bp)
    app.register_blueprint(orderRoutes.bp)
    
    return app