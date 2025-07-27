from flask import Blueprint, session, redirect, url_for, request, flash, render_template
from app import mongo
from bson.objectid import ObjectId
from app.utils.gemini_api import ask_gemini
import re
from datetime import datetime

coding_bp = Blueprint('coding', __name__)

@coding_bp.route('/study/<topic_id>/coding', methods=['GET', 'POST'])
@coding_bp.route('/study/<topic_id>/coding/<id>', methods=['GET', 'POST'])
def coding(topic_id, id=None):
	if 'user_id' not in session:
		flash('Please log in first to access the coding module.')
		return redirect(url_for('auth.login'))


	feedback = None
	prompt = None
	user_code = ""

	db = mongo.cx['intelligent_tutor']

	if request.method == 'POST':
		user_code = request.form['user_code']
		task = request.form['task']
		

		prompt = f'''
			Act as a professional professor for computer science. 
			You are an expert code evaluator.

			Here is a programming task on the topic "{topic_id}":
			{request.form['task']}

			Here is the code written by the student:
			{user_code}

			Please evaluate it for correctness, readability, and efficiency. Rate it from 0 to 100 and give feedback in this format:
			Score: <number>/100
			Feedback: <short summary>
		'''
		feedback = ask_gemini(prompt, user_id=session['user_id'], topic_id=topic_id, module="coding")

		db['code_results'].insert_one({
			"user_id": ObjectId(session['user_id']),
			"topic_id": topic_id,
			"code": user_code,
			"feedback": feedback,
			"timestamp": datetime.utcnow()
		})

		if id:
			db['review_tasks'].delete_one({'_id': ObjectId(id)})

	else:
		prompt = f'''Give me a short Python coding problem on the topic: {topic_id}. 
		Only describe the task. Keep it clear and beginner-friendly.'''
		task = ask_gemini(prompt, user_id=session['user_id'], topic_id=topic_id, module="coding")

	return render_template('coding/coding.html', topic_id=topic_id, task=task, feedback=feedback, user_code=user_code)		


