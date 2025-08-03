from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.utils.gemini_api import ask_gemini
from app import mongo
from bson.objectid import ObjectId
import datetime

teaching_bp = Blueprint('teaching', __name__)

@teaching_bp.route('/study/<topic_id>/teaching', methods=['GET', 'POST'])
@teaching_bp.route('/study/<topic_id>/teaching/<id>', methods=['GET', 'POST'])
def teaching(topic_id, id=None):
    if 'user_id' not in session:
        flash("Please log in to access the teaching module.")
        return redirect(url_for('auth.login'))

    feedback = None
    user_input = None

    if request.method == 'POST':
        user_input = request.form['explanation']
        topic_title = topic_id.replace('_', ' ').title()
        prompt = f'''
        Act as a professional professor in computer science, 
        with over 30 years of experience. Evaluate this 
        explanation of '{topic_title}' for a computer science student: 
        \"{user_input}\". What are the strong sides of the answer? 
        What is missing? Be honest, but constructive. 
        List out any gaps.'''
        feedback = ask_gemini(prompt)

        db = mongo.cx['intelligent_tutor']

        if id:
            db['review_tasks'].delete_one({'_id': ObjectId(id)})

        user_id = session['user_id']
        db['teaching_results'].insert_one({
            "user_id": ObjectId(user_id),
            "topic_id": topic_id,
            "user_input": user_input,
            "feedback": str(feedback),
            "timestamp": datetime.datetime.now(tz=datetime.UTC)
        })    


    return render_template('teaching/teaching.html', topic_id=topic_id, feedback=feedback, user_input=user_input)


    