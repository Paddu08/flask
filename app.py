from flask import Flask,request
from db import connection,cursor
app=Flask(__name__)


@app.get('/',)
def home():
     return ("hello world")
@app.post("/users")
def create_user():
    data = request.json
    username = data.get("username")

    cursor.execute(
        "INSERT INTO users (username) VALUES (%s) RETURNING id, username, created_at",
        (username,)
    )
    user = cursor.fetchone()
    return {"user": user}


# READ users
@app.get("/users")
def get_users():
    cursor.execute("SELECT id, username, created_at FROM users")
    users = cursor.fetchall()
    return {"users": users}
