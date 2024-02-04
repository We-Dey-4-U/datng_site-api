# app/models/messages.py
from app import db

class Messages(db.Model):
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))
    message_text = db.Column(db.Text)
    sent_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    is_read = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    reply_to = db.Column(db.Integer, db.ForeignKey('messages.message_id', ondelete='CASCADE'), nullable=True)
    forwarded_from = db.Column(db.Integer, db.ForeignKey('messages.message_id', ondelete='CASCADE'), nullable=True)

    sender = db.relationship('Users', foreign_keys=[sender_id], back_populates='sent_messages')
    receiver = db.relationship('Users', foreign_keys=[receiver_id], back_populates='received_messages')


   # Specify primaryjoin for reply relationship
    reply = db.relationship('Messages', 
                            #foreign_keys='reply_to',
                            foreign_keys=[reply_to],
                            remote_side=[message_id],
                            backref=db.backref("replies", lazy="dynamic"),
                            primaryjoin='Messages.message_id == Messages.reply_to')

    # Specify primaryjoin for forward relationship
    forward = db.relationship('Messages', 
                              #foreign_keys='forwarded_from',
                              foreign_keys=[forwarded_from],
                              remote_side=[message_id],
                              backref=db.backref("forwards", lazy="dynamic"),
                              primaryjoin='Messages.message_id == Messages.forwarded_from')



    def __init__(self, sender_id, receiver_id, message_text):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message_text = message_text