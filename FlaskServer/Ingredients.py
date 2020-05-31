from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

ingList = []
isFilter = False
name = "None"
tags = "None"

@ingredients.route("/ingredients")
def add_get_ingredients():
    isLogged = False
    if "user" in session:
        isLogged = True
    search_ingredient()
    return render_template("ingredients.html", ingList=ingList, isLogged=isLogged)

@ingredients.route("/addIngredient", methods=["POST"])
def add_ingredient():
    db = get_db()
    ingredient = serialize_ingredient(request.form)
    results = db.run("CREATE (i:INGREDIENTS {name:$name, tags:$tags})"
                    "RETURN i", {"name": ingredient.get("name"), "tags": ingredient.get("tags")})
    result = results.single()
    if result:
        flash(f"Se ingresó el ingrediente {ingredient.get('name')}", "info")
    else:
        flash("Ocurrió un error")
    return redirect(url_for("ingredients.add_get_ingredients"))

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

@ingredients.route("/filter_ingredient", methods=["POST"])
def filter_ingredient():
    global isFilter
    global name
    global tags
    name = request.form["name"]
    tags = request.form["tags"]
    if not name == "":
        isFilter = True
        flash(f"Filtrado por nombre: {name}")
    if not tags == "":
        isFilter = True
        flash(f"Filtrado por tags: {tags}")
    if (name == "") & (tags == ""):
        isFilter = False
    return redirect(url_for("ingredients.add_get_ingredients"))
    
def search_ingredient():
    ingList.clear()
    db = get_db()
    if not isFilter:
        results = db.run("MATCH (i:INGREDIENTS) RETURN i LIMIT 100")
        for record in results:
            ingList.append(serialize_ingredient(record[0]))
    else:
        query = "MATCH (i:INGREDIENTS)"
        if not name == "":
            query += " WHERE i.name CONTAINS " + "'" + name + "'"
        if not tags == "":
            if name == "":
                query += " WHERE i.tags CONTAINS " + "'" + tags + "'"
            else:
                query += " OR i.tags CONTAINS " + "'" + tags + "'"
        query += " RETURN i"
        results = db.run(query)
        for record in results:
            ingList.append(serialize_ingredient(record[0]))
        