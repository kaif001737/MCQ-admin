from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = "admin123"

client = MongoClient(os.getenv("MONGO_URI"))
db = client["mcq_system"]

# Admin login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["admin"] = True
            return redirect("/dashboard")
    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    users = list(db.users.find())
    results = list(db.results.find())
    return render_template("dashboard.html", users=users, results=results)

if __name__ == "__main__":
    app.run()