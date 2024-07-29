from flask import Blueprint, render_template, request, redirect, url_for
from app.models.product import Product
from app import db

bp = Blueprint('product', __name__)

@bp.route('/Product')
def index():
    data = Product.query.all()
    return render_template('products/index.html', data=data)

@bp.route('/Product/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        nombrepro = request.form['nombrepro']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        newProduct = Product(nombrepro=nombrepro, descripcion=descripcion, precio=precio, cantidad=cantidad)

        db.session.add(newProduct)
        db.session.commit()

        return redirect(url_for('product.index'))
                                
    return render_template('products/add.html')

@bp.route('/Product/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    product = Product.query.get_or_404(id)

    if request.method == 'POST':
        product.nombrepro = request.form['nombrepro']
        product.descripcion = request.form['descripcion']
        product.precio = request.form['precio']
        product.cantidad = request.form['cantidad']

        db.session.commit()

        return redirect(url_for('product.index'))
    
    return render_template('products/edit.html', product=product)

@bp.route('/Product/delete/<int:id>')
def delete(id):
    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('product.index'))