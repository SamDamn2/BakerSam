from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required
from app.models.factura import Factura
from app.models.detallefactura import Detallefactura
from app.routes.carritoRoutes import carrito_compras
from app import db

bp = Blueprint('factura', __name__)

@bp.route('/factura')
@login_required
def index():
    data = Factura.query.all()
    return render_template('facturas/index.html', data=data)
 

@bp.route('/addfactura', methods=['GET', 'POST'])
@login_required
def add():
    db.session.add(factura)
    db.session.commit()
    print("factura id  ", factura.idfactura)
    return redirect(url_for('factura.addDetalle',id=factura.idfactura))

@bp.route('/adddetalle/<int:id>', methods=['GET', 'POST'])
@login_required
def addDetalle(id):
    for item in carrito_compras.getItems():
        idproducto = item["producto"].idproducto
        cantidad = item["cantidad"]
        detallefactura = Detallefactura(idfactura=id, idproducto=idproducto, cantidad=cantidad)
        db.session.add(detallefactura)
    
    db.session.commit()  # Mover commit fuera del bucle para mejorar el rendimiento
    carrito_compras.vaciarcarrito()
    return redirect(url_for('producto.index'))


@bp.route('/factura/<int:id>', methods=['GET', 'POST'])
@login_required
def detalle(id):
    factura = Factura.query.get_or_404(id)
    detalle = factura.productos  # Cambiar `factura.producto` a `factura.productos`
    return render_template('detalles/index.html', data=detalle, factura=factura)


@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    factura = Factura.query.get_or_404(id)
    
    db.session.delete(factura)
    db.session.commit()

    return redirect(url_for('factura.index'))


