#!/usr/bin/env python
from json import dumps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from Logger import logger

app = Flask(__name__, static_url_path='/static/')
app.secret_key = "laura ya no!"
app.permanent_session_lifetime = timedelta(minutes=15) #it could be days="numero de dias"
app.register_blueprint(logger, url_prefix="/session")

@app.route("/")
def get_index():
    return app.send_static_file('index.html')

@app.route("/home")
def get_home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(port=8080, debug=True)
