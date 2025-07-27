from app import mongo
from bson.objectid import ObjectId
from datetime import datetime

def log_score(user_id, topic_id, module, score):
    performance_log = mongo.cx['intelligent_tutor']['performance_log']
    performance_log.insert_one({
        "user_id": ObjectId(user_id),
        "topic_id": topic_id,
        "module": module,
        "score": score,
        "timestamp": datetime.utcnow()
    })
