from app import mongo
from app.utils.gemini_api import ask_gemini
from datetime import datetime, timedelta
from bson.objectid import ObjectId
import json

def get_user_review_data(user_id):
    db = mongo.cx['intelligent_tutor']
    user_id = ObjectId(user_id)

    quiz = list(db.quiz_results.find({"user_id": user_id}))
    teach = list(db.teaching_results.find({"user_id": user_id}))
    code = list(db.code_results.find({"user_id": user_id}))

    data = {
        "quiz": quiz,
        "teaching": teach,
        "coding": code
    }

    return data


def suggest_review_task(user_id):
    user_data = get_user_review_data(user_id)

    prompt = f"""
    You are an intelligent review planner. Based on this data for a computer science student,
    suggest ONE topic they should review NOW, and the value of module from the values {{quiz, teaching, coding}}. 
    Respond ONLY in valid JSON, but your answer must be like a text, a string, and don't write any other words. Only the json with the values. Also, don't write ''' json ... ''', 
    only write the curly brackets and what is inside. Don't write in json format, write it as plain text, so that when I get your response using the API, I don't receive ``` json ... ```, as this is useless.

    Data:
    {user_data}

    Output format must be like this, what is written inside the double quotes, your response must not contain double quotes, and it must be plain text, not a json-formatted text:
    "
    {{
      "topic_id": "Stacks",
      "module": "Quiz"
    }}
    "
    """

    task_json = ask_gemini(prompt=prompt, user_id=str(user_id), module="review_engine")
    
    
    import json

    try:
        task = json.loads(task_json)
        task["user_id"] = ObjectId(user_id)
        task["created_at"] = datetime.utcnow()
        mongo.cx['intelligent_tutor']['review_tasks'].insert_one(task)

    except Exception as e:
        print(f"[Review Task] Failed to parse or store: {e}")    