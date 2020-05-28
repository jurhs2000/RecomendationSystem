from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

recomendations = Blueprint("recomendations", __name__, static_folder="static", template_folder="templates")

@recomendations.route("/recomendations")
def my_recomendations():
    if "user" in session:
        user = serialize_user(session["user"])
        myIngredients = []
        db = get_db()
        results = db.run("MATCH (:USER {username:$username})-[:USES]-(i:INGREDIENTS) RETURN i",
                        {"username": user.get("username")})
        for record in results:
            myIngredients.append(record[0].get("name"))
        return render_template("recomendations.html", user=user, myIngredients=myIngredients)
    else:
        flash("Inicia sesion primero")
        return redirect(url_for("logger.login"))

@recomendations.route("/remove_ingredient", methods=["POST"])
def remove_ingredient():
    user = serialize_user(session["user"])
    nameIngredient = request.form.get("value")
    db = get_db()
    db.run("MATCH (u:USER {username:$username}) MATCH (i:INGREDIENTS {name:$name}) MATCH (u)-[r:USES]->(i) DELETE r",
            {"username": user.get("username"), "name": nameIngredient})
    flash(f"{nameIngredient} ha sido removido de tu lista")
    return redirect(url_for("recomendations.my_recomendations"))