from dotenv import load_dotenv
from flask import Flask, session
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId



mongo = PyMongo()

def create_app():
    
    load_dotenv()
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['MONGO_URI'] = os.getenv("MONGO_URI")
    
    mongo.init_app(app)

    from .routes.default_page import default_bp
    app.register_blueprint(default_bp)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from .routes.study import study_bp
    app.register_blueprint(study_bp)

    from .routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)

    from .routes.teaching import teaching_bp
    app.register_blueprint(teaching_bp)

    from .routes.quiz import quiz_bp
    app.register_blueprint(quiz_bp)

    from .routes.coding import coding_bp
    app.register_blueprint(coding_bp)

    from app.tasks.scheduler import start_background_thread
    start_background_thread()

    @app.before_request
    def load_task_count():
        if 'user_id' in session:
            db = mongo.cx['intelligent_tutor']
            task_count = db.review_tasks.count_documents({
                "user_id": ObjectId(session['user_id'])
            })
        else:
            task_count = 0

    from app.routes.tasks import tasks_bp
    app.register_blueprint(tasks_bp)        

    return app