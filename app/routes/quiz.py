from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app.utils.quiz_generator import generate_quiz
from app.utils.performance_tracker import update_review_log
from bson.objectid import ObjectId
from app import mongo
import datetime


quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/study/<topic_id>/quiz', methods=['GET', 'POST'])
@quiz_bp.route('/study/<topic_id>/quiz/<id>', methods=['GET', 'POST'])
def quiz(topic_id, id=None):
    if 'user_id' not in session:
        flash('Please log in first to access the quiz page.')
        return redirect(url_for('auth.login'))

    topic_title = topic_id.replace('_', ' ').title()
    db = mongo.cx['intelligent_tutor']
    user_id=session['user_id']

    if request.method == 'POST':
        answers = request.form.to_dict()
        session['user_answers'] = answers
        quiz_data = eval(session.get('quiz_data', '[]'))
        correct = 0
        total = len(quiz_data)

        for q in quiz_data:
            user_answer = answers.get(q['question'], '').strip()
            if(user_answer.lower() == q['answer'].strip().lower()):
                correct += 1

        
        score = round((correct / total) * 100, 2)

        session['total_questions'] = total
        session['correct_count'] = correct
        session['incorrect_count'] = total-correct
        session['score'] = score
        


        db['quiz_results'].insert_one({
            "user_id": ObjectId(user_id),
            "topic_id": topic_id,
            "score": score,
            "submitted_answers": str(answers),
            "timestamp": datetime.datetime.now(tz=datetime.UTC)
        })

        if id:
            db['review_tasks'].delete_one({'_id': ObjectId(id)})  

        update_review_log(user_id, topic_id, score)
        return redirect(url_for('quiz.quiz_review', topic_id=topic_id, id=id))



    quiz_data = generate_quiz(topic_title)
    session['quiz_data'] = str(quiz_data)
    return render_template('quiz/quiz.html', topic_title=topic_title, topic_id=topic_id, quiz_data=quiz_data)

@quiz_bp.route('/study/<topic_id>/quiz/review', methods=['GET', 'POST'])
@quiz_bp.route('/study/<topic_id>/quiz/<id>/review', methods=['GET', 'POST'])
def quiz_review(topic_id, id=None):
    if 'user_id' not in session:
        flash("Please log in first.")
        return redirect(url_for('auth.login'))

    topic_title = topic_id.replace('_', ' ').title()
    quiz_data = eval(session.get('quiz_data', '[]'))
    user_answers = session.get('user_answers', {})
    score = session.get('score', 0)
    correct_count = session.get('correct_count', 0)
    incorrect_count = session.get('incorrect_count', 0)
    total_questions = session.get('total_questions', 0)

    return render_template('quiz/quiz_review.html', topic_title=topic_title, topic_id=topic_id, quiz_data=quiz_data, user_answers=user_answers, score=score, incorrect_count=incorrect_count, total_questions=total_questions, correct_count=correct_count)


