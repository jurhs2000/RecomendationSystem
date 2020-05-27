#!/usr/bin/env python
from json import dumps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__, static_url_path='/static/')
app.secret_key = "laura ya no!"
app.permanent_session_lifetime = timedelta(minutes=15) #it could be days="numero de dias"

@app.route("/")
def get_index():
    return app.send_static_file('index.html')

@app.route("/home")
def get_home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if (request.form.get("keep") == "isTrue"):
            session.permanent = True
        else:
            session.permanent = False
        user = request.form["name"]
        session["user"] = user
        flash("Sesion iniciada")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("La sesion ya esta iniciada")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Inicia sesion primero")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Sesion cerrada correctamente. Nos vemos pronto {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
