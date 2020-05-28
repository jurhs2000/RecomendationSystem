from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

meals = Blueprint("meals", __name__, static_folder="static", template_folder="templates")

@meals.route("/meals", methods=["POST", "GET"])
def add_get_meals():
    if request.method == "POST":
        return render_template("meals.html")
    else:
        return render_template("meals.html")