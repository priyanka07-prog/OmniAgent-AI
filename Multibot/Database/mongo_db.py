from pymongo import MongoClient 
client = MongoClient("mongodb://localhost:27017/")
db = client["multi_bot_db"]

chat_collection = db["chat_data"]

def save_chat_data(user_id, message, response):
    chat_collection.insert_one({
        "user_id": user_id,
        "message": message,
        "response": response
    })
