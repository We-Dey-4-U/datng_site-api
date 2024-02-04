# app/routes/matches_routes.py

from flask import Blueprint, jsonify, request
from app.services.match_service import create_match, get_matches_for_user, get_match, update_match, delete_match





matches_blueprint = Blueprint('matches', __name__)

@matches_blueprint.route('/create_match', methods=['POST'])
def create_match_route():
    data = request.get_json()
    user1_id = data.get('user1_id')
    user2_id = data.get('user2_id')
   
    try:
        create_match(user1_id, user2_id)  # Updated function call
        return jsonify({'message': 'Match created successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@matches_blueprint.route('/get_matches/<int:user_id>', methods=['GET'])
def get_matches_route(user_id):
    matches = get_matches_for_user(user_id)

    if matches:
        return jsonify({'matches': [{'match_id': match.match_id, 'user1_id': match.user1_id, 'user2_id': match.user2_id, 'user1_username': match.user1_username, 'user2_username': match.user2_username, 'matched_at': str(match.matched_at)} for match in matches]})
    else:
        return jsonify({'message': 'No matches found'}), 404

@matches_blueprint.route('/get_match/<int:match_id>', methods=['GET'])
def get_match_route(match_id):
    match = get_match(match_id)

    if match:
        return jsonify({'match_id': match.match_id, 'user1_id': match.user1_id, 'user2_id': match.user2_id, 'user1_username': match.user1_username, 'user2_username': match.user2_username, 'matched_at': str(match.matched_at)})
    else:
        return jsonify({'message': 'Match not found'}), 404

@matches_blueprint.route('/update_match/<int:match_id>', methods=['PATCH'])
def update_match_route(match_id):
    data = request.get_json()
    user1_id = data.get('user1_id')
    user2_id = data.get('user2_id')
    user1_username = data.get('user1_username')  # Updated parameter
    user2_username = data.get('user2_username')  # Updated parameter

    try:
        update_match(match_id, user1_id, user2_id, user1_username, user2_username)  # Updated function call
        return jsonify({'message': 'Match updated successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@matches_blueprint.route('/delete_match/<int:match_id>', methods=['DELETE'])
def delete_match_route(match_id):
    try:
        delete_match(match_id)
        return jsonify({'message': 'Match deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404