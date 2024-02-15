from pymongo import MongoClient

client = MongoClient ("mongodb+srv://todo:test12345@cluster0.rsslxqz.mongodb.net/?retryWrites=true&w=majority")

db = client.todo #бд

collection_name = db["todo_collection"]

#collection_name.insert_one({"_id": 1, "name":  "alex"})