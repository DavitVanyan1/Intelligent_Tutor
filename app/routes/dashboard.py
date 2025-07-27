from flask import Blueprint, render_template, url_for, session, redirect, flash
from app.utils.performance_tracker import get_random_review_topic

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in first")
        return redirect(url_for('auth.login'))
    review_topic = get_random_review_topic(session['user_id'])
    return render_template("study/dashboard.html", review_topic=review_topic)
