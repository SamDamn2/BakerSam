from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models.proveedor import Proveedor
from app import db

bp = Blueprint('proveedor', __name__)

@bp.route('/proveedor')
@login_required
def index():
    dataP = Proveedor.query.all()
    return render_template('proveedores/index.html', dataP=dataP)

@bp.route('/proveedor/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombrepvr = request.form['nombrepvr']
        cedulapvr = request.form['cedulapvr']
        telefonopvr = request.form['telefonopvr']
        
        proveedor = Proveedor(nombrepvr=nombrepvr, cedulapvr=cedulapvr, telefonopvr=telefonopvr)
        db.session.add(proveedor)
        db.session.commit()
        
        return redirect(url_for('proveedor.index'))

    return render_template('proveedores/add.html')

@bp.route('/proveedor/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombrepvr = request.form['nombrepvr']
        proveedor.cedulapvr = request.form['cedulapvr']
        proveedor.telefonopvr = request.form['telefonopvr']
        db.session.commit()
        return redirect(url_for('proveedor.index'))

    return render_template('proveedores/edit.html', proveedor=proveedor)

@bp.route('/proveedor/delete/<int:id>')
@login_required
def delete(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('proveedor.index'))