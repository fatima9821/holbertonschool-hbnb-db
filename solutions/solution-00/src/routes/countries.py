"""
This module contains the routes for the countries endpoint
"""

from flask import Blueprint
from src.controllers.countries import (
    get_countries,
    get_country_by_code,
    get_country_cities,
)

countries_bp = Blueprint("countries", __name__, url_prefix="/countries")

@countries_bp.route("/", methods=["GET"])
@jwt_required()
def get_countries_protected():
    return jsonify(get_countries()), 200

@countries_bp.route("/<code>", methods=["GET"])
@jwt_required()
def get_country_by_code_protected(code):
    return get_country_by_code(code)

@countries_bp.route("/<code>/cities", methods=["GET"])
@jwt_required()
def get_country_cities_protected(code):
    return get_country_cities(code)
