# app/services/virtual_gifts_service.py
from app.models.virtual_gifts import VirtualGifts
from app import db

def send_virtual_gift(sender_id, receiver_id, gift_name):
    new_gift = _create_virtual_gift(sender_id, receiver_id, gift_name)
    _broadcast_virtual_gift(sender_id, receiver_id, gift_name, new_gift.sent_at)

def get_gifts_for_user(user_id):
    return VirtualGifts.query.filter((VirtualGifts.sender_id == user_id) | (VirtualGifts.receiver_id == user_id)).all()

def delete_gift(gift_id):
    gift = VirtualGifts.query.get(gift_id)
    if gift:
        db.session.delete(gift)
        db.session.commit()
    else:
        raise ValueError("Virtual gift not found")

def _create_virtual_gift(sender_id, receiver_id, gift_name):
    new_gift = VirtualGifts(sender_id=sender_id, receiver_id=receiver_id, gift_name=gift_name)
    db.session.add(new_gift)
    db.session.commit()
    return new_gift

def mark_gift_as_received(gift_id):
    gift = VirtualGifts.query.get(gift_id)

    if gift:
        gift.received_at = db.func.current_timestamp()
        db.session.commit()
    else:
        raise ValueError("Gift not found")

def _broadcast_virtual_gift(sender_id, receiver_id, gift_name, sent_at):
    # Add broadcasting logic here if needed
    pass