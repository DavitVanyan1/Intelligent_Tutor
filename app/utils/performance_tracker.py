from datetime import datetime, timedelta
from app import mongo
from bson.objectid import ObjectId
import random

def get_topics_for_review(user_id):
    db = mongo.cx['intelligent_tutor']
    review_log = db['review_log']
    review_docs = list(review_log.find({"user_id": ObjectId(user_id)}))
    overdue = []
    for doc in review_docs:
        if doc.get("score", 100) < 80 or (datetime.utcnow() - doc["last_reviewed"]).days > 3:
            overdue.append(doc["topic_id"])
    return overdue

def get_random_review_topic(user_id):
    topics = get_topics_for_review(user_id)
    return random.choice(topics) if topics else None

def get_topic_difficulty(user_id, topic_id):
    db = mongo.cx['intelligent_tutor']
    review_log = db['review_log']
    records = review_log.find({"user_id": ObjectId(user_id), "topic_id": topic_id})
    scores = [rec.get("score", 100) for rec in records]
    if not scores:
        return "medium"
    avg = sum(scores) / len(scores)
    if avg < 60:
        return "hard"
    elif avg < 80:
        return "medium"
    else:
        return "easy"




def update_review_log(user_id, topic_id, new_score):
    db = mongo.cx['intelligent_tutor']
    log = db.review_log.find_one({"user_id": ObjectId(user_id), "topic_id": topic_id})

    if log:
        db.review_log.update_one(
            {"_id": log['_id']},
            {"$set": {"score": new_score, "last_reviewed": datetime.utcnow()}}
        )
    else:
        db.review_log.insert_one({
            "user_id": ObjectId(user_id),
            "topic_id": topic_id,
            "score": new_score,
            "last_reviewed": datetime.utcnow()
        })
