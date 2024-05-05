
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os
import json

load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

uri = f"mongodb+srv://{username}:{password}@cluster0.7whr0zh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.bookkeeping
collection = db.billing

def insertData(data):
    result = collection.insert_one(data)
    
    if result.acknowledged:
        print({"staus": True, "message": "success"})
    else:
        print({"status": False, "message": "something wrong"})

def findData(pageSize=10, pageNum=0):
    results = []
    cursor = collection.find().skip(pageSize * (pageNum - 1)).limit(10)
    for doc in cursor:
        doc["_id"] = str(doc["_id"])
        
        results.append(doc)
    return results
