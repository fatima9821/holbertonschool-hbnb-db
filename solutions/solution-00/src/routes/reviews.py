"""
This module contains the routes for the reviews blueprint
"""

from flask import Blueprint
from src.controllers.reviews import (
    create_review,
    delete_review,
    get_reviews_from_place,
    get_reviews_from_user,
    get_review_by_id,
    get_reviews,
    update_review,
)

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/places/<place_id>/reviews", methods=["POST"])
@jwt_required()
def create_review_protected(place_id):
    return create_review(place_id)

@reviews_bp.route("/places/<place_id>/reviews", methods=["GET"])
@jwt_required()
def get_reviews_from_place_protected(place_id):
    return get_reviews_from_place(place_id)

@reviews_bp.route("/users/<user_id>/reviews", methods=["GET"])
@jwt_required()
def get_reviews_from_user_protected(user_id):
    return get_reviews_from_user(user_id)

@reviews_bp.route("/reviews", methods=["GET"])
@jwt_required()
def get_reviews_protected():
    return get_reviews()

@reviews_bp.route("/reviews/<review_id>", methods=["GET"])
@jwt_required()
def get_review_by_id_protected(review_id):
    return get_review_by_id(review_id)

@reviews_bp.route("/reviews/<review_id>", methods=["PUT"])
@jwt_required()
def update_review_protected(review_id):
    return update_review(review_id)

@reviews_bp.route("/reviews/<review_id>", methods=["DELETE"])
@jwt_required()
def delete_review_protected(review_id):
    claims = get_jwt()
    if not claims.get("is_admin"):
        return jsonify({"msg": "Admin privilege required"}), 403
    return delete_review(review_id)
