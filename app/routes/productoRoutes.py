from flask import Blueprint, render_template, request, redirect, url_for
from app.models.producto import Producto
from app.routes.carritoRoutes import carrito_compras

from app import db

bp = Blueprint('producto', __name__)

@bp.route('/')
def index():
    data = Producto.query.all()   
    return render_template('productos/index.html', data=data,t=carrito_compras.tamañoD())

@bp.route('/Producto/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombrepdo = request.form['nombrepdo']
        descripcionpdo = request.form['descripcionpdo']
        preciopdo = request.form['preciopdo']
        stockpdo = request.form['stockpdo']
        
        newProducto = Producto(nombrepdo=nombrepdo, descripcionpdo=descripcionpdo, preciopdo=preciopdo, stockpdo=stockpdo)
        db.session.add(newProducto)
        db.session.commit()
        
        return redirect(url_for('producto.index'))

    return render_template('productos/add.html')

@bp.route('/Producto/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombrepdo = request.form['nombrepdo']
        producto.descripcionpdo = request.form['descripcionpdo']
        producto.preciopdo = request.form['preciopdo']
        producto.stockpdo = request.form['stockpdo']
        db.session.commit()
        return redirect(url_for('producto.index'))

    return render_template('productos/edit.html', producto=producto)
    

@bp.route('/Producto/delete/<int:id>')
def delete(id):
    producto = Producto.query.get_or_404(id)
    
    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('producto.index'))
@bp.route('/Producto/Listar/<int:id>', methods=['GET', 'POST'])
def list(id):
    producto = Producto.query.get_or_404(id)  # Obtener el producto por su ID

    if request.method == 'POST':
        producto.nombrepdo = request.form['nombrepdo']
        producto.descripcionpdo = request.form['descripcionpdo']
        producto.preciopdo = request.form['preciopdo']
        producto.stockpdo = request.form['stockpdo']
        db.session.commit()
        return redirect(url_for('producto.index'))

    # Renderizar la plantilla con los detalles del producto
    return render_template('productos/list.html', producto=producto)

    