from app import mongo
from app.utils.gemini_api import ask_gemini
import datetime
from bson.objectid import ObjectId

def create_topic(topic_id):
	db = mongo.cx['intelligent_tutor']

	if db['topics'].find_one({'_id': topic_id}):
		return None

	prompt = f'''
	Act as a professional computer science professor in an Ivy league university. Write a full, detailed, professional and informative text about {topic_id}. This text should be crafted as an educational content, so that people can read it and as a result learn and understand the topic fully and to the highest level. You are encouraged to use various trustworthy sources, like textbooks, papers or other sources that are absolutely trustworthy and contain the needed information. You are also free to use these websites as well:
	https://www.w3schools.com/
	https://www.geeksforgeeks.org/
	https://developer.mozilla.org/en-US/
	https://www.tutorialspoint.com/

	Write only the material for learning. So, begin your response immidiately with the learning content. Write nothing else. Your response will be immidiately be shown to learners, so they don't need to see any other text except the learning content. 
	'''

	content = ask_gemini(prompt)

	db['topics'].insert_one({
		'_id': topic_id,
		'name': topic_id.capitalize(),
		'learning_content': content,
		'created_at': datetime.datetime.now(datetime.UTC)
	})
