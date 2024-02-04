# app/services/message_service.py
from app.models.messages import Messages
from app import db, socketio

def send_private_message(sender_id, receiver_id, message_text, reply_to=None):
    if reply_to:
        message_text = _prepend_reply_text(reply_to, message_text)

    new_message = _create_message(sender_id, receiver_id, message_text)
    _broadcast_private_message(sender_id, receiver_id, message_text, new_message.sent_at, reply_to)

def mark_message_as_read(message_id):
    message = Messages.query.get(message_id)
    if message:
        message.is_read = True
        db.session.commit()
    else:
        raise ValueError("Message not found")

def forward_message(sender_id, receiver_id, message_id):
    original_message = Messages.query.get(message_id)
    if original_message:
        forwarded_text = _prepend_forwarded_text(original_message.message_text)
        send_private_message(sender_id, receiver_id, forwarded_text)
    else:
        raise ValueError("Original message not found")

def delete_message(message_id):
    message = Messages.query.get(message_id)
    if message:
        db.session.delete(message)
        db.session.commit()
    else:
        raise ValueError("Message not found")

def _prepend_reply_text(reply_to, message_text):
    original_message = Messages.query.get(reply_to)
    if original_message:
        return f"Replying to: {original_message.message_text}\n\n{message_text}"
    return message_text

def _create_message(sender_id, receiver_id, message_text):
    new_message = Messages(sender_id=sender_id, receiver_id=receiver_id, message_text=message_text)
    db.session.add(new_message)
    db.session.commit()
    return new_message

def _broadcast_private_message(sender_id, receiver_id, message_text, sent_at, reply_to):
    message_data = {
        'sender_id': sender_id,
        'receiver_id': receiver_id,
        'message_text': message_text,
        'sent_at': str(sent_at),
        'reply_to': reply_to
    }
    socketio.emit('private_message', message_data, room=sender_id)
    socketio.emit('private_message', message_data, room=receiver_id)