# app/routes/virtual_gifts_routes.py
from flask import Blueprint, jsonify, request
from app.services.virtual_gifts_service import send_virtual_gift, get_gifts_for_user, delete_gift,  mark_gift_as_received

virtual_gifts_blueprint = Blueprint('virtual_gifts', __name__)

@virtual_gifts_blueprint.route('/send_virtual_gift', methods=['POST'])
def send_virtual_gift_route():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    gift_name = data.get('gift_name')

    try:
        send_virtual_gift(sender_id, receiver_id, gift_name)
        return jsonify({'message': 'Virtual gift sent successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@virtual_gifts_blueprint.route('/get_gifts/<int:user_id>', methods=['GET'])
def get_gifts_for_user_route(user_id):
    gifts = get_gifts_for_user(user_id)

    if gifts:
        return jsonify({'gifts': [{'gift_id': gift.gift_id, 'sender_id': gift.sender_id, 'receiver_id': gift.receiver_id, 'gift_name': gift.gift_name, 'sent_at': str(gift.sent_at)} for gift in gifts]})
    else:
        return jsonify({'message': 'No virtual gifts found'}), 404

@virtual_gifts_blueprint.route('/delete_gift/<int:gift_id>', methods=['DELETE'])
def delete_gift_route(gift_id):
    try:
        delete_gift(gift_id)
        return jsonify({'message': 'Virtual gift deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


@virtual_gifts_blueprint.route('/mark_gift_received/<int:gift_id>', methods=['PATCH'])
def mark_gift_received_route(gift_id):
    try:
        mark_gift_as_received(gift_id)
        return jsonify({'message': 'Gift marked as received successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404