from flask import Blueprint, render_template

bp = Blueprint('menu', __name__)

@bp.route('/vista')
def vista():
    return render_template('menu/base.html')

@bp.route('/restaurante')
def restaurante():
    return render_template('menu/restaurante.html')

@bp.route('/panaderia')
def panaderia():
    return render_template('menu/panaderia.html')

@bp.route('/cafeteria')
def cafeteria():
    return render_template('menu/cafeteria.html')
