from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

recomendations = Blueprint("recomendations", __name__, static_folder="static", template_folder="templates")


myIngredients = []
basicRecomend = []
tastes = []
kinds = []
styles = []
isFilter = False
taste = "None"
kind = "None"
style = "None"

@recomendations.route("/recomendations")
def my_recomendations():
    if "user" in session:
        user = serialize_user(session["user"])
        get_recomendations()
        return render_template("recomendations.html", user=user, myIngredients=myIngredients,
                                basicRecomend=basicRecomend, tastes=tastes, kinds=kinds, styles=styles)
    else:
        flash("Inicia sesión primero")
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

@recomendations.route("/filter", methods=["POST"])
def filter():
    global isFilter
    global taste
    global kind
    global style
    taste = request.form["taste"]
    kind = request.form["kind"]
    style = request.form["style"]
    if not taste == "None":
        isFilter = True
        flash(f"Filtrado por sabor: {taste}")
    if not kind == "None":
        isFilter = True
        flash(f"Filtrado por tipo: {kind}")
    if not style == "None":
        isFilter = True
        flash(f"Filtrado por metodo: {style}")
    if (taste == "None") & (kind == "None") & (style == "None"):
        isFilter = False
    return redirect(url_for("recomendations.my_recomendations"))

def get_recomendations():
    myIngredients.clear()
    basicRecomend.clear()
    tastes.clear()
    kinds.clear()
    styles.clear()
    user = serialize_user(session["user"])
    db = get_db()
    results = db.run("MATCH (:USER {username:$username})-[:USES]-(i:INGREDIENTS) RETURN i",
                    {"username": user.get("username")})
    for record in results:
        myIngredients.append(record[0].get("name"))
    print(isFilter)
    if not isFilter:
        # Recomendacion basica
        results = db.run("MATCH (:USER {username:$username})-[:USES]->(i:INGREDIENTS)-[r:IS_USED_IN]->(m:MEAL)"
                        "RETURN m,count(r) AS count ORDER BY count DESC", {"username":user.get("username")})
        for record in results:
            meal = serialize_meal(record[0])
            results = db.run("MATCH (i:INGREDIENTS)-[:IS_USED_IN]->(m:MEAL {name:$name}) RETURN count(i) AS count",
                            {"name": meal.get("name")})
            ingredientsCount = results.single()
            meal["coincidence"] = (record[1] * 100) / ingredientsCount[0]
            basicRecomend.append(meal)
    else:
        # Recomendacion filtrada
        parameters = {"username": user.get("username")}
        query = "MATCH (:USER {username:$username})-[:USES]->(i:INGREDIENTS)-[r:IS_USED_IN]->(m:MEAL)"
        if not taste == "None":
            query += " MATCH (m)-[:TASTE]->(:TASTE {name:$taste})"
            parameters["taste"] = taste
        if not kind == "None":
            query += " MATCH (m)-[:IS_A]->(:KIND {name:$kind})"
            parameters["kind"] = kind 
        if not style == "None":
            query += " MATCH (m)-[:METHOD]->(:STYLES {name:$style})"
            parameters["style"] = style
        query += " RETURN m, count(r) AS count ORDER BY count"
        results = db.run(query, parameters)
        for record in results:
            meal = serialize_meal(record[0])
            results = db.run("MATCH (i:INGREDIENTS)-[:IS_USED_IN]->(m:MEAL {name:$name}) RETURN count(i) AS count",
                            {"name": meal.get("name")})
            ingredientsCount = results.single()
            meal["coincidence"] = (record[1] * 100) / ingredientsCount[0]
            basicRecomend.append(meal)
    basicRecomend.sort(key=lambda x: x.get("coincidence"), reverse=True)
    results = db.run("MATCH (t:TASTE) RETURN t")
    for record in results:
        tastes.append(record[0]["name"])
    results = db.run("MATCH (k:KIND) RETURN k")
    for record in results:
        kinds.append(record[0]["name"])
    results = db.run("MATCH (s:STYLES) RETURN s")
    for record in results:
        styles.append(record[0]["name"])