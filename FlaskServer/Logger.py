from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

logger = Blueprint("logger", __name__, static_folder="static", template_folder="templates")

@logger.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("keep") == "isTrue":
            session.permanent = True
        else:
            session.permanent = False
        user = serialize_user(request.form)
        db = get_db()
        results = db.run("MATCH (user:User {username:$username, password:$password})"
                        "RETURN user", {"username": user.get("username"), "password": user.get("password")})
        result = results.single()
        if result == None:
            flash("No se ha podido iniciar sesion")
            return redirect(url_for("logger.login"))
        else:
            flash(f"Sesion iniciada correctamente, Hola {serialize_user(result[0]).get('name')}!")
            session["user"] = serialize_user(result[0])
            return redirect(url_for("recomendations.my_recomendations"))
    else:
        if "user" in session:
            flash("La sesion ya esta iniciada")
            return redirect(url_for("recomendations.my_recomendations"))
        return render_template("login.html")

@logger.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = serialize_user(request.form)
        db = get_db()
        results = db.run("CREATE (user:User {name:$name, username:$username, password:$password})"
                        "RETURN user", {"name": user.get("name"), "username": user.get("username"),
                        "password": user.get("password")})
        result = results.single()
        if result:
            session["user"] = user
            flash(f"Bienvenido a la experiencia {user.get('name')}", "info")
            return redirect(url_for("recomendations.my_recomendations"))
        else:
            flash("ocurrio un error")
    else:
        if "user" in session:
            flash("La sesion ya esta iniciada")
            return redirect(url_for("recomendations.my_recomendations"))
        return render_template("register.html")

@logger.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Sesion cerrada correctamente. Nos vemos pronto {user.get('name')}", "info")
    session.pop("user", None)
    return redirect(url_for("logger.login"))