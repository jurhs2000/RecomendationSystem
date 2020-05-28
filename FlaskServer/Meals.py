from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

meals = Blueprint("meals", __name__, static_folder="static", template_folder="templates")

@meals.route("/meals", methods=["POST", "GET"])
def add_get_meals():
    if request.method == "POST":
        return render_template("meals.html")
    else:
        mealsList = []
        db = get_db()
        results = db.run("MATCH (m:MEAL) WITH m LIMIT 100 MATCH (i:INGREDIENTS)-[:IS_USED_IN]->(m) RETURN m, i")
        for record in results:
            isIn = False
            meal = serialize_meal(record[0])
            ingredient = serialize_ingredient(record[1])
            for m in mealsList:
                if m.get("name") == meal.get("name"):
                    m.get("ingredients").append(ingredient)
                    isIn = True
            if not isIn:
                meal.get("ingredients").append(ingredient)
                mealsList.append(meal)
        results = db.run("MATCH (m:MEAL) WITH m LIMIT 100 MATCH (m)-[:TASTE]->(t:TASTE) RETURN m, t")
        for record in results:
            meal = serialize_meal(record[0])
            for m in mealsList:
                if m.get("name") == meal.get("name"):
                    m.get("tastes").append(record[1]["name"])
        results = db.run("MATCH (m:MEAL) WITH m LIMIT 100 MATCH (m)-[:IS_A]->(k:KIND) RETURN m, k")
        for record in results:
            meal = serialize_meal(record[0])
            for m in mealsList:
                if m.get("name") == meal.get("name"):
                    m.get("kinds").append(record[1]["name"])
        results = db.run("MATCH (m:MEAL) WITH m LIMIT 100 MATCH (m)-[:METHOD]->(s:STYLES) RETURN m, s")
        for record in results:
            meal = serialize_meal(record[0])
            for m in mealsList:
                if m.get("name") == meal.get("name"):
                    m.get("styles").append(record[1]["name"])
        return render_template("meals.html", mealsList=mealsList)