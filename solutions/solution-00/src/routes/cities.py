"""
This module contains the routes for the cities blueprint
"""

from flask import Blueprint
from src.controllers.cities import (
    create_city,
    delete_city,
    get_city_by_id,
    get_cities,
    update_city,
)

cities_bp = Blueprint("cities", __name__, url_prefix="/cities")

@cities_bp.route("/", methods=["GET"])
@jwt_required()
def get_cities_protected():
    return jsonify(get_cities()), 200

@cities_bp.route("/", methods=["POST"])
@jwt_required()
def create_city_protected():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    return create_city()

@cities_bp.route("/<city_id>", methods=["GET"])
@jwt_required()
def get_city_by_id_protected(city_id):
    return get_city_by_id(city_id)

@cities_bp.route("/<city_id>", methods=["PUT"])
@jwt_required()
def update_city_protected(city_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    return update_city(city_id)

@cities_bp.route("/<city_id>", methods=["DELETE"])
@jwt_required()
def delete_city_protected(city_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Admin access required"}), 403
    return delete_city(city_id)
