from app import mongo


def create_user(username, email, password_hash):
    db = mongo.cx['intelligent_tutor']
    users_collection = db['users']
    users_collection.insert_one({
        'username': username,
        'email': email,
        'password': password_hash
    })

def get_user_by_username(username):
    db = mongo.cx['intelligent_tutor']['users']
    return db.find_one({'username': username})

def get_user_by_email(email):
    db = mongo.cx['intelligent_tutor']
    users_collection = db['users']
    return users_collection.find_one({'email': email})

