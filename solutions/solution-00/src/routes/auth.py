""" classe authentification """

from flask import Blueprint, request, jsonify
from src.models.user import User
from flask_jwt_extended import create_access_token
from src import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad credentials"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin', False)

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already registered"}), 400

    user = User(email=email, is_admin=is_admin)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201
