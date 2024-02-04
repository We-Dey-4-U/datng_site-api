# app/models/user.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from flask_login import UserMixin
from app.models.messages import Messages 
from app import db, bcrypt  # Import db and bcrypt

class Users(db.Model, UserMixin):  # Use db.Model as the base class
    __tablename__ = 'Users'
    user_id = Column(db.Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


    

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