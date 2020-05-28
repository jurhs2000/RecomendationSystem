from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort, Response
from Serialized_Models import *
from Connection import *

recomendations = Blueprint("recomendations", __name__, static_folder="static", template_folder="templates")


@recomendations.route("/recomendations")
def my_recomendations():
    if "user" in session:
        user = serialize_user(session["user"])
        return render_template("recomendations.html", user=user)
    else:
        flash("Inicia sesion primero")
        return redirect(url_for("logger.login"))