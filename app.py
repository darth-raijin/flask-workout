import os
from flask import Flask, session, request, redirect, render_template, url_for, flash
from flask_login import login_required, current_user, LoginManager
from flask_session import Session
from dotenv import load_dotenv
from datetime import date

import sys
import uuid
import random
import json
from blueprints.auth import auth
from util import builder
from services.database import Database
from models.user import User


load_dotenv()
database = Database()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

mongo = database.get_mongo()
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo.init_app(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

builder.load_colors()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Registering blueprints
app.register_blueprint(auth)




@login_manager.user_loader
def load_user(user_id):
        try:
                result = database.get_user_by_id(user_id)
                user = User(id = result["id"], email = result["email"],
                joined_rooms = result["joined_rooms"], friends = result["friends"])
                return user
        except:
                return None

@login_required
@app.route("/current")
def current():
        name = current_user.get_id()
        return f"Name: {name}"

@app.route('/')
def index():
        return render_template("index.html")

@login_required
@app.route("/profile")
def profile():
        user_profile = database.get_user_by_id(current_user.get_id())
        user_rooms = database.get_room_by_user(current_user.get_id())

        user_profile["friend_count"] = len(user_profile["friends"])
        user_profile["room_count"] = len(user_profile["joined_rooms"])
        print(len(user_profile["joined_rooms"]))
        return render_template("profile.html", rooms = user_rooms, profile = user_profile) 

@login_required
@app.route("/settings")
def settings():
        return render_template("settings.html") 

@login_required
@app.route("/me")
def me():
        return current_user.get_all()


if __name__ == '__main__':
    socketio.run(threaded=True)