from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

mongo = PyMongo()


class Database:

    def __init__(self):
        return

    def get_mongo(self):
        # Used in app.py to set configs
        print("Mongo retrieved")
        return mongo

    def get_user_by_id(self, user_id: str):
        result = mongo.db.users.find({"_id": user_id})
        result_dict = {}

        # TODO Change to result.get

        result_dict = {
            }
        print(result_dict)
        if not result_dict:
            return None

        return result_dict

    def create_user(self, user_id: str, email: str, password: str):
        try:
            result = mongo.db.users.insert_one(
                {"_id": user_id, "email": email, "password": password})
            return True
        except:
            return False

    def create_workout(user_id: str, current_date: str):
        ""


