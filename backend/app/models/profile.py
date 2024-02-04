# app/models/profile.py
from app import db

class Profiles(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)
    interests = db.Column(db.String(255))
    profile_picture_url = db.Column(db.String(255))
    location = db.Column(db.String(100))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    user = db.relationship('Users', back_populates='profile')