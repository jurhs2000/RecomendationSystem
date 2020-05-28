from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

@ingredients.route("/ingredients", methods=["POST", "GET"])
def add_get_ingredients():
    if request.method == "POST":
        return render_template("ingredients.html")
    else:
        ingList = []
        db = get_db()
        results = db.run("MATCH (n:INGREDIENTS) RETURN n LIMIT 100")
        for record in results:
            ingList.append(serialize_ingredient(record[0]))
        return render_template("ingredients.html", ingList=ingList)