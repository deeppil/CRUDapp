from pymongo import MongoClient

MONGO_URL = "mongodb+srv://deepakpil2006_db_user:UZMdudfEWTVdtt7W@crudapp.epfnwri.mongodb.net/?appName=CRUDapp"
client = MongoClient(MONGO_URL)

db = client["student_db"]
student_collection = db["students"]