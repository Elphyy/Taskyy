from flask import render_template
from app import app
from app import database as data


@app.route("/")
def homepage():
    connection = data.db_connection("localhost", "root", "elphyy")
    return render_template("index.html", todos=data.get_todos(connection))
