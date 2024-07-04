"""
This module contains the routes for the admin blueprint
"""

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route("/data", methods=["POST", "DELETE"])
@jwt_required()
def admin_data():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    # Admin-only functionality here
    return jsonify({"msg": "Admin access granted"}), 200
