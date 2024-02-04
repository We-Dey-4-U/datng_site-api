# app/services/match_service.py

from app.models.matches import Matches
from app.models.user import Users 
from app import db

def create_match(user1_id, user2_id):
    user1 = db.session.query(Users).get(user1_id)
    user2 = db.session.query(Users).get(user2_id)

    new_match = Matches(
        user1_id=user1_id,
        user2_id=user2_id,
        user1_username=user1.username,  # Assuming there is a 'username' field in the Users model
        user2_username=user2.username,
    )

    db.session.add(new_match)
    db.session.commit()

def get_matches_for_user(user_id):
    matches = Matches.query.filter((Matches.user1_id == user_id) | (Matches.user2_id == user_id)).all()
    return matches

def get_match(match_id):
    return Matches.query.get(match_id)

def update_match(match_id, user1_id, user2_id, user1_username, user2_username):  # Updated function parameters
    match = Matches.query.get(match_id)
    if match:
        match.user1_id = user1_id
        match.user2_id = user2_id
        match.user1_username = user1_username  # Updated model field
        match.user2_username = user2_username  # Updated model field
        db.session.commit()
    else:
        raise ValueError("Match not found")

def delete_match(match_id):
    match = Matches.query.get(match_id)
    if match:
        db.session.delete(match)
        db.session.commit()
    else:
        raise ValueError("Match not found")