from app import db

class Icebreakers(db.Model):
    __tablename__ = 'Icebreakers'
    icebreaker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    icebreaker_text = db.Column(db.Text)
    category = db.Column(db.String(255))
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='SET NULL'))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    
    creator = db.relationship('Users', foreign_keys=[creator_id], back_populates='created_icebreakers')


    def __init__(self, icebreaker_text, category, creator_id=None):
        self.icebreaker_text = icebreaker_text
        self.category = category
        self.creator_id = creator_id