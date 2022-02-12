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
@workout.route("/")
def workout_root():
    if request.method == "POST":
        # Upon creating a new workout, BE will handle creation and redirect the user to the new workout

        current_date = datetime.today().strftime('%d-%m-%y')
        created_workout = database.create_workout(current_user.get_id(), current_date)

        if created_workout != False:
            # Redirected to the view for the created workout
            current_app.logger.info(f"Created workout for user: {current_user.get_id()}")
            return redirect(url_for("view_workout", id = created_workout))
        
        return redirect(url_for("workout_root"))

    if request.method == "GET":
        if request.args.get("fail") != None:
            flash("That workout is not")
        return render_template("workout_root.html")

@login_required
@workout.route("/view")
def view_workout():
    # Route displays the workout details, and associated exercises
    if request.method == "POST":
        # Posting new exercises to the workout
        ""
    if request.method == "PUT":
        # Updating the workout details
        # Weight and date
        ""
    
    if request.method == "GET":
        if request.args.get("id") != None:
            current_app.logger.info(f"Fetching workout with id: {request.args.get('id')}")
            fetched_workout = database.get_workout_by_id(request.args.get('id'))
