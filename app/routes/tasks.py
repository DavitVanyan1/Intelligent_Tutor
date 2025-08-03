from flask import Blueprint, render_template, session, redirect, url_for
from app import mongo
from bson.objectid import ObjectId

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks')
def tasks():
    if 'user_id' not in session:
        flash("Please log in to access the tasks section.")
        return redirect(url_for('auth.login'))


    db = mongo.cx['intelligent_tutor']
    tasks = db['review_tasks'].find({
        "user_id": ObjectId(session['user_id'])
    }).sort("created_at", 1)

    return render_template("tasks/tasks.html", tasks=tasks)    