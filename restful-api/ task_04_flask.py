#!/usr/bin/python3
"""This module uses Flask to create a simple RESTFULAPI"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Returns list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns OK status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns user data by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user via POST"""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201
