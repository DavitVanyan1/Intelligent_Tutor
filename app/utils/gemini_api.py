from google import genai
import os
from dotenv import load_dotenv
from datetime import datetime
from app import mongo
from bson.objectid import ObjectId

load_dotenv()


def ask_gemini(prompt, user_id=None, topic_id=None, module=None):
    try:

        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        text = response.text

        
        db = mongo.cx['intelligent_tutor']
        ai_feedback = db['ai_feedback']
        ai_feedback.insert_one({
            "user_id": ObjectId(user_id),
            "topic_id": topic_id,
            "module": module,
            "prompt": prompt,
            "response": text,
            "timestamp": datetime.utcnow()
        })
            
        return text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return f"Gemini Error: {e}"