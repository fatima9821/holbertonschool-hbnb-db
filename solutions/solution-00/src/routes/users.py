"""
This module contains the routes for the users endpoints.
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@users_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify(user.to_dict())

@users_bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    data = request.get_json()
    user = User.create(data)
    return jsonify(user.to_dict()), 201

@users_bp.route('/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    data = request.get_json()
    user = User.update(user_id, data)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify(user.to_dict())

@users_bp.route('/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    if not User.delete(user_id):
        return jsonify({"msg": "User not found"}), 404
    return '', 204

