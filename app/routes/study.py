from flask import Blueprint, render_template, session, redirect, url_for
from app.models.topic_model import get_all_topics, get_topic_by_id, modules

study_bp = Blueprint('study', __name__)


@study_bp.route('/study')
def study_home():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    topics = get_all_topics()
    return render_template('study/topics_list.html', topics=topics)

@study_bp.route('/study/<topic_id>/<module>')
def study_module(topic_id, module):
    topic = get_topic_by_id(topic_id)
    if not topic or module not in modules:
        return redirect(url_for('study.study_home'))
    
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

