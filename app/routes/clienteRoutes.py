from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models.cliente import Cliente
from app import db

bp = Blueprint('clientes', __name__)

@bp.route('/clientes')
@login_required
def index():
    data = Cliente.query.all()
    return render_template('clientes/index.html', data=data)

@bp.route('/clientes/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombrecte = request.form['nombrecte']
        direccioncte = request.form['direccioncte']
        telefonocte = request.form['telefonocte']
        
        cliente = Cliente(nombrecte=nombrecte, direccioncte=direccioncte, telefonocte=telefonocte)
        db.session.add(cliente)
        db.session.commit()
        
        return redirect(url_for('clientes.index'))

    return render_template('clientes/add.html')

@bp.route('/clientes/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombrecte = request.form['nombrecte']
        cliente.direccioncte = request.form['direccioncte']
        cliente.telefonocte = request.form['telefonocte']
        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('clientes/edit.html', cliente=cliente)

@bp.route('/clientes/delete/<int:id>')
@login_required
def delete(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.index'))