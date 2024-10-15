from pymongo import MongoClient


mongo_client = MongoClient("mongodb://172.29.168.75:27017/")
users_db = mongo_client['users-db']


users = users_db["users"]