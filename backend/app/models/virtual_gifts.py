# app/models/virtual_gifts.py
from app import db

class VirtualGifts(db.Model):
    __tablename__ = 'VirtualGifts'
    gift_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))
    gift_name = db.Column(db.String(50))
    sent_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    received_at = db.Column(db.TIMESTAMP, nullable=True) 

    sender = db.relationship('Users', foreign_keys=[sender_id], back_populates='sent_gifts')
    receiver = db.relationship('Users', foreign_keys=[receiver_id], back_populates='received_gifts')

    def __init__(self, sender_id, receiver_id, gift_name):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.gift_name = gift_name