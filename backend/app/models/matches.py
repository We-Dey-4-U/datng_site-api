# app/models/matches.py

from app import db

class Matches(db.Model):
    __tablename__ = 'matches'
    match_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))
    user2_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'))
    user1_username = db.Column(db.String(50))  # Add this line
    user2_username = db.Column(db.String(50))  # Add this line
    matched_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())


    user1 = db.relationship('Users', foreign_keys=[user1_id])
    user2 = db.relationship('Users', foreign_keys=[user2_id])