from flask import Blueprint, render_template
from flask_login import login_required
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.routes.carritoRoutes import carrito_compras



bp = Blueprint('menu', __name__)

@bp.route('/vista')
def vista():
    return render_template('menu/base.html')

@bp.route('/cafeteria')
@login_required
def cafeteria():
    productos = Producto.query.join(Categoria).filter(Categoria.tipocga == 'Cafetería').all()
    return render_template('menu/cafeteria.html', productos=productos, t=carrito_compras.tamañoD())

@bp.route('/restaurante')
@login_required
def restaurante():
    productos = Producto.query.join(Categoria).filter(Categoria.tipocga == 'Restaurante').all()
    return render_template('menu/restaurante.html', productos=productos, t=carrito_compras.tamañoD())

@bp.route('/panaderia')
@login_required
def panaderia():
    productos = Producto.query.join(Categoria).filter(Categoria.tipocga == 'Panadería').all()
    return render_template('menu/panaderia.html', productos=productos, t=carrito_compras.tamañoD())

