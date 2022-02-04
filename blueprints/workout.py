from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from models import user
import re
from services.database import Database
from models.user import User
from datetime import datetime

workout = Blueprint('workout', __name__, url_prefix='/workout',
                 static_folder="static", template_folder="/workout/")
database = Database()

@login_required
@workout.route("(/")
def workout_root():
    if request.method == "POST":
        # Upon creating a new workout, BE will handle creation and redirect the user to the new workout

        current_date = datetime.today().strftime('%d-%m-%y')
        database.create_workout(current_user.get_id(), current_date)


    if request.method == "GET":
        return render_template("workout_root.html")