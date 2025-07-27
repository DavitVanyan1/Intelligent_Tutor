from app.utils.gemini_api import ask_gemini
import json

def generate_quiz(topic_title, difficulty='medium'):
    prompt = f'''
    Act as a professional professor in computer science, with over 40 years of experience. 
    Generate a {difficulty} quiz for the topic: '{topic_title}' Make sure the questions are 
    well-structured to evaluate the knowledge of the computer science student with the given quiz.
    Create 5 questions. Types of questions are 'multiple_choice' or 'true_false',
    Also, Write the response as a plain text, not a json formatted response, so that when
    I receive your response from the API, I don't get ``` json ... ``` as well,
    as this will be problematic for me. Just return your answer as plain text. 
    Return the quiz questions in JSON format, don't write anything else 
    except the questions, so your response must be like:
    
    [
        {{
            "question": "What is a stack?",
            "type": "multiple_choice",
            "options": ["FIFO", "LIFO", "Queue", "Heap"],
            "answer": "LIFO"
        }},
        {{
            "question": "Stacks use FIFO. (True/False)",
            "type": "true_false",
            "answer": "False"
        }},
        {{
            "question": "Fill in the blank: A stack follows the ____ principle.",
            "type": "multiple_choice",
            "options": ["FIFO", "LIFO", "Queue", "Heap"],
            "answer": "LIFO"
        }}
    ]
    
    And most importantly, return your answer as plain text, not JSON-formatted.
    '''

    response = ask_gemini(prompt)
    print(str(response))
    try:
        result = json.loads(response)
        return result
    except Exception as e:
        print("Parsing quiz error:", e)
        return []
