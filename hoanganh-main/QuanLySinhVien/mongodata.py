from pymongo import MongoClient

# db_connection.py
from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["university"]
    return db
