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
        result = mongo.db.users.find_one({"_id": user_id})
        print(result)
        result_dict = {
                "id": result.get("_id"),
                "email": result.get("email"),
                "password": result.get("password")
                }
        print(result_dict)
        if not result_dict:
            return None

        return result_dict

    def create_user(self, user_id: str, email: str, password: str):
        try:
            result = mongo.db.users.insert_one(
                {"_id": user_id, "email": email, "password": password})
            print(f"Result for DB create_user: %s" % result)
            return True
        except:
            print("Error inserting user")
            return False

    def create_workout(user_id: str, current_date: str):
        """Used to add a workout and connect it to the creating user

        Args:
            user_id (str): Username for the current user
            current_date (str): Current date in dd/mm/yyyy format

        Returns:
            str: id for the created workout
        """
        try:
            result = mongo.db.workouts.insert_one(
                {"user": user_id, "current_date": current_date,
                "weight": 0, "exercises": []})
            return str(result.inserted_id)
        except:
            return False

    def get_workout_by_id(id: str):
        fetched_workout = mongo.db.users.find({"_id": id})
        result_dict = {}

        # TODO Change to result.get

        result_dict = {
                "id": result_dict.get("_id"),
                "email": result_dict.get("email"),
                "password": result_dict.get("password")
                }
        print(result_dict)
        if not result_dict:
            return None

        return result_dict
