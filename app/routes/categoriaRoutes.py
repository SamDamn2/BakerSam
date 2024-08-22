from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.categoria import Categoria
from app import db

bp = Blueprint('categoria', __name__)

@bp.route('/Categoria')
def index():
    dataC = Categoria.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    return render_template('categorias/index.html', dataC=dataC)

@bp.route('/Categoria/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        tipocga = request.form['tipocga']
        
        newCate = Categoria(tipocga=tipocga)
        db.session.add(newCate)
        db.session.commit()
        
        return redirect(url_for('categoria.index'))

    return render_template('categorias/add.html')

@bp.route('/Categoria/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    categoria = Categoria.query.get_or_404(id)

    if request.method == 'POST':
        categoria.tipocga = request.form['tipocga']
        db.session.commit()
        return redirect(url_for('categoria.index'))

    return render_template('categorias/edit.html', categoria=categoria)
    

@bp.route('/Categoria/delete/<int:id>')
def delete(id):
    categoria = Categoria.query.get_or_404(id)
    
    db.session.delete(categoria)
    db.session.commit()

    return redirect(url_for('categoria.index'))