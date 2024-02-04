# app/auth.py

from app.models.user import Users

def load_user(user_id):
    return Users.query.get(int(user_id))