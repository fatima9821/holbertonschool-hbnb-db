"""
This module contains the routes for the users endpoints.
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

users_bp = Blueprint("users", __name__, url_prefix="/users")

# Utilisation de jwt_required pour sécuriser la route get_users
@users_bp.route("/", methods=["GET"])
@jwt_required()
def get_users_protected():
    users = get_users()
    return jsonify(users), 200

users_bp.route("/", methods=["POST"])(create_user)
users_bp.route("/<user_id>", methods=["GET"])(get_user_by_id)
users_bp.route("/<user_id>", methods=["PUT"])(update_user)
users_bp.route("/<user_id>", methods=["DELETE"])(delete_user)