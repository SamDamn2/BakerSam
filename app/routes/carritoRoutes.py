from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.models.producto import Producto
from app.models.carrito import Carrito
from app.models.factura import Factura
from app.models.detallefactura import Detallefactura
from app import db

bp = Blueprint('carrito', __name__)
carrito_compras = Carrito()

@bp.route('/ListarCarrito')
@login_required
def listar():
    items = carrito_compras.getItems()
    return render_template('productos/list.html', items=items)

@bp.route('/ListarProductos')
@login_required
def index():
    producto = carrito_compras
    return render_template('index.html', producto=producto)

@bp.route('/agregar/<int:id>', methods=['POST'])
@login_required
def agregar_al_carrito(id):
    cantidad = int(request.form['cantidad'])
    carrito_compras.agregar_producto(id, cantidad)
    return redirect(url_for('producto.index'))
    #return "Entra a agregar corrito"

@bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_del_carrito(id):
    carrito_compras.eliminar_producto(id)
    return redirect(url_for('carrito.listar'))

@bp.route('/realizar_compra')
@login_required
def realizar_compra():
    total = carrito_compras.calcular_total()
    return render_template('carritos/realizar_compra.html', total=total)


@bp.route('/generar_factura', methods=['POST'])
@login_required
def generar_factura():
    total = carrito_compras.calcular_total()
    
    # Obtener el ID del cliente (aquí debes obtener el ID del cliente de alguna manera)
    id_cliente = 1  # Aquí debes obtener el ID del cliente, por ejemplo, de la sesión del usuario
    
    # Crear una nueva factura
    factura = Factura(fechafta='Hoy', idcliente=id_cliente)
    db.session.add(factura)
    db.session.commit()  # Guardar la factura para obtener el ID
    
    # Agregar detalles de la factura
    for item in carrito_compras.getItems():
        detallefactura = Detallefactura(
            idfactura=factura.idfactura,
            idproducto=item['producto'].idproducto,
            cantidad=item['cantidad']
        )
        db.session.add(detallefactura)
    
    db.session.commit()  # Guardar todos los detalles de la factura
    
    # Vaciar el carrito de compras
    carrito_compras.carrito = []
    
    return render_template('carritos/factura.html', total=total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
@login_required
def tCarrito():
    a = carrito_compras.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_compras.tamañoD()}"