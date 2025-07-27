from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import create_user, get_user_by_username, get_user_by_email


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if get_user_by_username(username):
            flash('Username already exists.')
            return redirect(url_for('auth.signup'))

        if get_user_by_email(email):
            flash('Username already exists.')
            return redirect(url_for('auth.signup'))
        
        password_hash = generate_password_hash(password)
        create_user(username, email, password_hash)
        flash('You have signed up successfully. Please log in.')
        return redirect(url_for('auth.login'))

    return render_template("auth/signup.html")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user_by_username(username)
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['email'] = user['email']
            session['initials'] = ''.join([n[0].upper() for n in user['username'].split('_')])
            flash('You have logged in successfully!')
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Incorrect username or password')

    return render_template("auth/login.html")

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully')
    return redirect(url_for('auth.login'))


