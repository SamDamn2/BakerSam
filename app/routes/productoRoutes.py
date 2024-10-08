from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename
from app.models.proveedor import Proveedor
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.routes.carritoRoutes import carrito_compras
from app import db
import os

bp = Blueprint('producto', __name__)

@bp.route('/producto')
@login_required
def index():
    data = Producto.query.all()
    dataC = Categoria.query.all()
    dataP = Proveedor.query.all()
    return render_template('productos/index.html', data=data, dataC=dataC, dataP=dataP, t=carrito_compras.tamañoD())

@bp.route('/vista')
@login_required
def vista():
    data = Producto.query.all()
    dataC = Categoria.query.all()
    dataP = Proveedor.query.all()
    return render_template('menu/base.html', data=data, dataC=dataC, dataP=dataP, t=carrito_compras.tamañoD())

@bp.route('/Producto/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombrepdo = request.form['nombrepdo']
        idproveedor = request.form['nombrepvr']
        idcategoria = request.form['tipocga']
        descripcionpdo = request.form['descripcionpdo']
        preciopdo = request.form['preciopdo']
        stockpdo = request.form['stockpdo']

        imagenpdo = request.files['imagenpdo']

        if imagenpdo:
            filename = secure_filename(imagenpdo.filename)
            imagen_path = os.path.join('static', 'img', filename)
            imagenpdo.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = imagen_path
        else:
            ruta_imagen = None

        newProducto = Producto(nombrepdo=nombrepdo, idcategoria=idcategoria, idproveedor=idproveedor, descripcionpdo=descripcionpdo, preciopdo=preciopdo, stockpdo=stockpdo, imagenpdo=imagenpdo.filename)
        db.session.add(newProducto)
        db.session.commit()

        categoria = Categoria.query.get(idcategoria)
        if categoria:
            if categoria.tipocga == 'Cafetería':
                return redirect(url_for('menu.cafeteria'))
            elif categoria.tipocga == 'Restaurante':
                return redirect(url_for('menu.restaurante'))
            elif categoria.tipocga == 'Panadería':
                return redirect(url_for('menu.panaderia'))

        return redirect(url_for('producto.index'))
    categorias = Categoria.query.all()
    proveedores = Proveedor.query.all()
    return render_template('productos/add.html', categorias=categorias, proveedores=proveedores)

@bp.route('/Producto/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    producto = Producto.query.get_or_404(id)
    categorias = Categoria.query.all()
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        producto.nombrepdo = request.form['nombrepdo']
        producto.idcategoria = request.form['tipocga']
        producto.idproveedor = request.form['nombrepvr']
        producto.descripcionpdo = request.form['descripcionpdo']
        producto.preciopdo = request.form['preciopdo']
        producto.stockpdo = request.form['stockpdo']
        db.session.commit()
        return redirect(url_for('producto.index'))

    return render_template('productos/edit.html', producto=producto, categorias=categorias, proveedores=proveedores)
    

@bp.route('/Producto/delete/<int:id>')
@login_required
def delete(id):
    producto = Producto.query.get_or_404(id)
    
    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('producto.index'))
@bp.route('/Producto/Listar/<int:id>', methods=['GET', 'POST'])
@login_required
def list(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombrepdo = request.form['nombrepdo']
        producto.idcategoria = request.form['tipocga']
        producto.idproveedor = request.form['nombrepvr']
        producto.descripcionpdo = request.form['descripcionpdo']
        producto.preciopdo = request.form['preciopdo']
        producto.stockpdo = request.form['stockpdo']
        db.session.commit()
        return redirect(url_for('producto.index'))

    # Renderizar la plantilla con los detalles del producto
    return render_template('productos/list.html', producto=producto)

    