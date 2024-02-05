# app/routes/auth.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.authentication import register_user, login_user
from app.models.user import Users
from app.auth import load_user  # Import load_user from auth.py
from app import db

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    creator_id = data.get('creator_id')  # Include creator_id in the request

    try:
        register_user(username, email, password, creator_id=creator_id)
        return jsonify({'message': 'User created successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    remember = data.get('remember', False)

    user = login_user(username, password, remember=remember)

    if user:
        access_token = create_access_token(identity=user.user_id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@auth_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200