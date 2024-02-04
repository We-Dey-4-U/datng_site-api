# app/services/profile.py
from app.models.profile import Profiles
from app import db

def create_profile(user_id, first_name, last_name, age, bio, interests, profile_picture_url, location):
    new_profile = Profiles(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        age=age,
        bio=bio,
        interests=interests,
        profile_picture_url=profile_picture_url,
        location=location
    )

    db.session.add(new_profile)
    db.session.commit()

def get_profile_by_user_id(user_id):
    return Profiles.query.filter_by(user_id=user_id).first()

def update_profile(user_id, data):
    profile = Profiles.query.filter_by(user_id=user_id).first()

    if profile:
        for key, value in data.items():
            setattr(profile, key, value)

        db.session.commit()
    else:
        raise ValueError("Profile not found")

def delete_profile(user_id):
    profile = Profiles.query.filter_by(user_id=user_id).first()

    if profile:
        db.session.delete(profile)
        db.session.commit()
    else:
        raise ValueError("Profile not found")