from app.models.icebreakers import Icebreakers
from app import db

def create_icebreaker(icebreaker_text, category, creator_id=None):
    new_icebreaker = Icebreakers(icebreaker_text=icebreaker_text, category=category, creator_id=creator_id)
    db.session.add(new_icebreaker)
    db.session.commit()
    return new_icebreaker

def get_icebreakers():
    return Icebreakers.query.all()

def get_icebreaker(icebreaker_id):
    return Icebreakers.query.get(icebreaker_id)

def update_icebreaker(icebreaker_id, icebreaker_text, category):
    icebreaker = Icebreakers.query.get(icebreaker_id)
    if icebreaker:
        icebreaker.icebreaker_text = icebreaker_text
        icebreaker.category = category
        db.session.commit()
    else:
        raise ValueError("Icebreaker not found")

def delete_icebreaker(icebreaker_id):
    icebreaker = Icebreakers.query.get(icebreaker_id)
    if icebreaker:
        db.session.delete(icebreaker)
        db.session.commit()
    else:
        raise ValueError("Icebreaker not found")