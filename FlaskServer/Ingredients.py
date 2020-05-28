from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

@ingredients.route("/ingredients", methods=["POST", "GET"])
def add_get_ingredients():
    if request.method == "POST":
        return render_template("ingredients.html")
    else:
        isLogged = False
        if "user" in session:
            isLogged = True
        ingList = []
        db = get_db()
        results = db.run("MATCH (n:INGREDIENTS) RETURN n LIMIT 100")
        for record in results:
            ingList.append(serialize_ingredient(record[0]))
        return render_template("ingredients.html", ingList=ingList, isLogged=isLogged)

@ingredients.route("/addToUser", methods=["POST"])
def add_to_user():
    db = get_db()
    alreadyIn = False
    nameIngredient = request.form.get("value")
    user = session["user"]
    results = db.run("MATCH (u:USER {username:$username})-[:USES]->(i:INGREDIENTS) RETURN i",
                    {"username": user.get("username")})
    for record in results:
        if record[0].get("name") == nameIngredient:
            alreadyIn = True
    if not alreadyIn:
        db.run("MATCH (u:USER {username:$username}) MATCH (i:INGREDIENTS {name:$name}) CREATE (u)-[:USES]->(i)",
                {"username": user.get("username"), "name": nameIngredient})
        flash(f"{nameIngredient} añadido a tu lista")
        return redirect(url_for("recomendations.my_recomendations"))
    else:
        flash(f"{nameIngredient} ya está en tu lista")
        return redirect(url_for("ingredients.add_get_ingredients"))
    