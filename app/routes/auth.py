from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.personal import Personal

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombreperso = request.form['nombreperso']
        passwordperso = request.form['passwordperso']
        
        personal = Personal.query.filter_by(nombreperso=nombreperso, passwordperso=passwordperso).first()

        if personal:
            login_user(personal)
            flash("Login successful!", "success")
            return redirect(url_for('auth.dashboard'))
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    return render_template("/personal/login.html")

@auth_bp.route('/vista')
@login_required
def dashboard():
    return redirect(url_for('auth.dashboard'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
