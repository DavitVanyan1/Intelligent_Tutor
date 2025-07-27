from flask import Blueprint, render_template, session, url_for, redirect

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for("auth.login"))

    return redirect(url_for("dashboard.dashboard"))