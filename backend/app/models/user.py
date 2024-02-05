# app/models/user.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from flask_login import UserMixin
from app.models.messages import Messages
from app.models.virtual_gifts import VirtualGifts
from app.models.icebreakers import Icebreakers  # Move the import here
from app import db, bcrypt  # Import db and bcrypt

class Users(db.Model, UserMixin):  # Use db.Model as the base class
    __tablename__ = 'Users'
    user_id = Column(db.Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))

    # Implement UserMixin methods
    def get_id(self):
        return str(self.user_id)

    def check_password(self, password):
        # Use the correct attribute name for password_hash
        return bcrypt.check_password_hash(self.password_hash, password)

    @classmethod
    def query(cls, session=None):
        session = session or db.session
        return session.query(cls)

    profile = db.relationship('Profiles', back_populates='user')
    sent_messages = db.relationship('Messages', foreign_keys='Messages.sender_id', back_populates='sender')
    received_messages = db.relationship('Messages', foreign_keys='Messages.receiver_id', back_populates='receiver')
    sent_gifts = db.relationship('VirtualGifts', foreign_keys=[VirtualGifts.sender_id], back_populates='sender')
    received_gifts = db.relationship('VirtualGifts', foreign_keys=[VirtualGifts.receiver_id], back_populates='receiver')
    created_icebreakers = db.relationship('Icebreakers', foreign_keys=[Icebreakers.creator_id], back_populates='creator')
    #created_users = db.relationship('Users', back_populates='creator', foreign_keys=[Users.creator_id])
    

    


  