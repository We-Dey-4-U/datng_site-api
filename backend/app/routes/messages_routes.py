# app/routes/messages_routes.py
from flask import Blueprint, jsonify, request
from app.services.message_service import (
    send_private_message, 
    mark_message_as_read, 
    delete_message, 
    forward_message
)

messages_blueprint = Blueprint('messages', __name__)

@messages_blueprint.route('/send_private_message', methods=['POST'])
def send_private_message_route():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message_text = data.get('message_text')
    reply_to = data.get('reply_to')

    try:
        send_private_message(sender_id, receiver_id, message_text, reply_to=reply_to)
        return jsonify({'message': 'Private message sent successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@messages_blueprint.route('/mark_as_read/<int:message_id>', methods=['PATCH'])
def mark_message_as_read_route(message_id):
    try:
        mark_message_as_read(message_id)
        return jsonify({'message': 'Message marked as read'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@messages_blueprint.route('/delete_message/<int:message_id>', methods=['DELETE'])
def delete_message_route(message_id):
    try:
        delete_message(message_id)
        return jsonify({'message': 'Message deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@messages_blueprint.route('/forward_message', methods=['POST'])
def forward_message_route():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message_id = data.get('message_id')

    try:
        forward_message(sender_id, receiver_id, message_id)
        return jsonify({'message': 'Message forwarded successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400