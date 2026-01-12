from pymongo import MongoClient

MONGO_URL = "mongodb+srv://USERNAME:PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)

db = client["student_db"]
student_collection = db["students"]