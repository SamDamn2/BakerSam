from flask import Blueprint, render_template, request, redirect, url_for
from app.models.order import Order
from app import db

bp = Blueprint('order', __name__)

@bp.route('/')
def index():
    data = Order.query.all()
    return render_template('orders/index.html', data=data)

@bp.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        fecha = request.form['fecha']
        preciototal = request.form['preciototal']

        newOrder = Order(fecha=fecha, preciototal=preciototal)

        db.session.add(newOrder) 
        db.session.commit()

        return redirect(url_for('order.index'))
                                
    return render_template('orders/add.html')

@bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    order = Order.query.get_or_404(id)

    if request.method == 'POST':
        order.fecha = request.form['fecha']
        order.preciototal = request.form['preciototal']

        db.session.commit()

        return redirect(url_for('order.index'))
    
    return render_template('orders/edit.html', order=order)

@bp.route('/delete/<int:id>')
def delete(id):
    order = Order.query.get_or_404(id)

    db.session.delete(order)
    db.session.commit()

    return redirect(url_for('order.index'))