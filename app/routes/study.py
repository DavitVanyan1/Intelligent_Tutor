from flask import Blueprint, render_template, session, redirect, url_for
from app.models.topic_model import get_all_topics, get_topic_by_id, modules
from app.utils.topic_creator import create_topic
from app import mongo

study_bp = Blueprint('study', __name__)



@study_bp.route('/study')
@study_bp.route('/study/<theme>')
def study_home(theme=None):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    topics = get_all_topics(filter_by_name=theme)
    return render_template('study/topics_list.html', topics=topics, theme=theme)

@study_bp.route('/study/<topic_id>/<module>')
def study_module(topic_id, module):

    create_topic(topic_id)
    topic = get_topic_by_id(topic_id)
    
    module_name_map = {
        "learn": "Learn",
        "quiz": "Quiz",
        "teach": "Teach",
        "code": "Code"
    }

    return render_template(
        f'study/module_{module}.html',
        topic=topic,
        module_name=module_name_map[module]
    )