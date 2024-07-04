"""
Users controller module
"""

from flask import abort, request, jsonify
from src.models.user import User
from src import db, bcrypt

def get_users():
    """Returns all users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

def create_user():
    """Creates a new user"""
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        abort(400, "Missing required fields: email and password")

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

    return jsonify(new_user.to_dict()), 201

def get_user_by_id(user_id):
    """Returns a user by ID"""
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")
    return jsonify(user.to_dict())

def update_user(user_id):
    """Updates a user by ID"""
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    data = request.get_json()
    if data.get('email'):
        user.email = data['email']
    if data.get('password'):
        user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    if data.get('is_admin') is not None:
        user.is_admin = data['is_admin']

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

    return jsonify(user.to_dict())

def delete_user(user_id):
    """Deletes a user by ID"""
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

    return '', 204