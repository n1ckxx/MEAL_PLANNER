import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URL')
client = MongoClient(MONGO_URI)
db = client.meal_planner

def insert_user_profile(profile_data):
    db.user_profiles.insert_one(profile_data)

def update_user_profile(user_id, profile_data):
    db.user_profiles.update_one({"user_id": user_id}, {"$set": profile_data})

def get_user_profile(user_id):
    return db.user_profiles.find_one({"user_id": user_id})

def insert_meal_plan(meal_plan):
    db.meal_plans.insert_one(meal_plan)

def get_meal_plans():
    return db.meal_plans.find()

def insert_feedback(feedback):
    db.feedback.insert_one(feedback)

def insert_rating_comment(meal_plan_id, user_id, rating, comment):
    db.ratings_comments.insert_one({
        "meal_plan_id": meal_plan_id,
        "user_id": user_id,
        "rating": rating,
        "comment": comment
    })

def get_ratings_comments(meal_plan_id=None):
    if meal_plan_id:
        return db.ratings_comments.find({"meal_plan_id": meal_plan_id})
    else:
        return db.ratings_comments.find()
