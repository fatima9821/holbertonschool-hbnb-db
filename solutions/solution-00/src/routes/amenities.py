"""
This module contains the routes for the amenities blueprint
"""

from flask import Blueprint
from src.controllers.amenities import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

amenities_bp = Blueprint("amenities", __name__, url_prefix="/amenities")

@amenities_bp.route("/", methods=["GET"])
@jwt_required()
def get_amenities_protected():
    return jsonify(get_amenities()), 200

@amenities_bp.route("/", methods=["POST"])
@jwt_required()
def create_amenity_protected():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    return create_amenity()

@amenities_bp.route("/<amenity_id>", methods=["GET"])
@jwt_required()
def get_amenity_by_id_protected(amenity_id):
    return get_amenity_by_id(amenity_id)

@amenities_bp.route("/<amenity_id>", methods=["PUT"])
@jwt_required()
def update_amenity_protected(amenity_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    return update_amenity(amenity_id)

@amenities_bp.route("/<amenity_id>", methods=["DELETE"])
@jwt_required()
def delete_amenity_protected(amenity_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    return delete_amenity(amenity_id)
