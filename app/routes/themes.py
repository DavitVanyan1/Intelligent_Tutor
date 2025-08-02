from flask import Blueprint, render_template, redirect, url_for
from app.models.topic_model import get_all_topics, get_topic_by_id, modules

themes_bp = Blueprint('themes', __name__)

themes = [
    {
        "id": "data_structures", 
        "name": "Data Structures"
    },
    {
        "id": "algorithms", 
        "name": "Algorithms"
    }
]

@themes_bp.route('/themes')
def themes():
    themes = get_all_topics()
    return render_template('themes/themes.html', themes=themes)

@themes_bp.route('/themes/<theme_id>')
def theme_redirect(theme_id):
    return redirect(url_for('study.study_home', theme=theme_id))