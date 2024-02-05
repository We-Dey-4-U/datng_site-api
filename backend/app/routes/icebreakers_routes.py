from flask import Blueprint, jsonify, request
from app.services.icebreaker_service import create_icebreaker, get_icebreakers, get_icebreaker, update_icebreaker, delete_icebreaker

icebreakers_blueprint = Blueprint('icebreakers', __name__)

@icebreakers_blueprint.route('/create_icebreaker', methods=['POST'])
def create_icebreaker_route():
    data = request.get_json()
    icebreaker_text = data.get('icebreaker_text')
    category = data.get('category')
    creator_id = data.get('creator_id')

    try:
        new_icebreaker = create_icebreaker(icebreaker_text, category, creator_id)
        return jsonify({'message': 'Icebreaker created successfully', 'icebreaker': {'icebreaker_id': new_icebreaker.icebreaker_id, 'icebreaker_text': new_icebreaker.icebreaker_text, 'category': new_icebreaker.category, 'creator_id': new_icebreaker.creator_id, 'created_at': str(new_icebreaker.created_at)}}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@icebreakers_blueprint.route('/get_icebreakers', methods=['GET'])
def get_icebreakers_route():
    icebreakers = get_icebreakers()

    if icebreakers:
        return jsonify({'icebreakers': [{'icebreaker_id': icebreaker.icebreaker_id, 'icebreaker_text': icebreaker.icebreaker_text, 'category': icebreaker.category, 'creator_id': icebreaker.creator_id, 'created_at': str(icebreaker.created_at)} for icebreaker in icebreakers]})
    else:
        return jsonify({'message': 'No icebreakers found'}), 404

@icebreakers_blueprint.route('/get_icebreaker/<int:icebreaker_id>', methods=['GET'])
def get_icebreaker_route(icebreaker_id):
    icebreaker = get_icebreaker(icebreaker_id)

    if icebreaker:
        return jsonify({'icebreaker_id': icebreaker.icebreaker_id, 'icebreaker_text': icebreaker.icebreaker_text, 'category': icebreaker.category, 'creator_id': icebreaker.creator_id, 'created_at': str(icebreaker.created_at)})
    else:
        return jsonify({'message': 'Icebreaker not found'}), 404

@icebreakers_blueprint.route('/update_icebreaker/<int:icebreaker_id>', methods=['PATCH'])
def update_icebreaker_route(icebreaker_id):
    data = request.get_json()
    icebreaker_text = data.get('icebreaker_text')
    category = data.get('category')

    try:
        update_icebreaker(icebreaker_id, icebreaker_text, category)
        return jsonify({'message': 'Icebreaker updated successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@icebreakers_blueprint.route('/delete_icebreaker/<int:icebreaker_id>', methods=['DELETE'])
def delete_icebreaker_route(icebreaker_id):
    try:
        delete_icebreaker(icebreaker_id)
        return jsonify({'message': 'Icebreaker deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404