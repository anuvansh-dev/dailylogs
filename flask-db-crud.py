"""
Connecting Flask to a database(SQLite)
- CRUD Operations with Flask and SQLite
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Setup db uri for sqlite
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# Initializing SQLAlchemy
db = SQLAlchemy(app)

# Define a user model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Creating the table in the test db
with app.app_context():
    db.create_all()

# Create a new user (POST request)
@app.route("/user", methods=["POST"])
def add_user():
    name = request.json["name"]
    age = request.json["age"]
    
    # Creating a new user object
    new_user = User(name=name, age=age)

    # add the new user to the db session
    db.session.add(new_user)

    # commit the transaction
    db.session.commit()

    return jsonify({"message": "User added successfully!", "user": {"name": name, "age": age}})

# Get all users (GET request)
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()

    user_list = [{"id": user.id, "name": user.name, "age": user.age} for user in users]

    return jsonify({"users": user_list})

# Get a specific user by id (GET request)
@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "age": user.age})
    else:
        return jsonify({"message": "User not found!"}), 404

# Update an existing user's details (PUT request)
@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)

    if user:
        data = request.get_json()
        user.name = data["name"]
        user.age = data["age"]
        db.session.commit()
        return jsonify({"message": "User updated successfully!"})
    return jsonify({"message": "User not found!"}), 404

# Delete a user (DELETE request)
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully!"})
    return jsonify({"message": "User not found!"}), 404


if __name__ == "__main__":
    app.run(debug=True)