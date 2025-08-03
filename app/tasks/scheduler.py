from threading import Thread
from time import sleep
from app import mongo
from app.utils.review_suggestion import suggest_review_task
from bson.objectid import ObjectId

def task_worker():
    while True:
        db = mongo.cx['intelligent_tutor']
        users = db['users'].find({})

        for user in users:
            user_id = str(user['_id'])
            suggest_review_task(user_id)

        sleep(60 * 60 * 8)

def start_background_thread():
    t = Thread(target=task_worker)
    t.daemon = True
    t.start()