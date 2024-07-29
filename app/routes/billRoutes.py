from flask import Blueprint, render_template, request, redirect, url_for
from app.models.product import Product
from app.models.order import Order
from app.models.bill import Bill
from sqlalchemy import text
from app import db

bp = Blueprint('bill', __name__)

@bp.route('/Bill')
def index():
    data = Bill.query.all()
    products = Product.query.all()
    orders = Order.query.all()

    return render_template('bills/index.html', data=data, products=products, orders=orders)

@bp.route('/addBill', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        product_id = request.form['product_id']
        order_id = request.form['order_id']
        nombreprodu = request.form['nombreprodu']
        cantidad = request.form['cantidad']
        preciouni = request.form['preciouni']
        subtotal = request.form['subtotal']

        newBill = Bill(orders=product_id, products=order_id, nombreprodu=nombreprodu, cantidad=cantidad, preciouni=preciouni, subtotal=subtotal)

        db.session.add(newBill)
        db.session.commit()

        return redirect(url_for('bill.index'))
    
    products = Product.query.all()
    orders =  Order.query.all()
    return render_template('bills/add.html', products=products, orders=orders)