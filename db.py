
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
        print("插入成功")
    else:
        print("插入失败")


# insertData({
#     "date": "2024-05-03",
#     "item": "groceries",
#     "cost": 15,
#     "description": "今天买菜花费15元"
# })

print(json.loads("""
{
    "date": "2024-05-03",
    "item": "午餐",
    "cost": 15,
    "description": "中午吃饭的费用"
}
"""))