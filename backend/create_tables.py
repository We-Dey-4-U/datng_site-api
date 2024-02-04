# create_tables.py
from app import create_app, db
from app.models.messages import Messages

# Create the Flask app
app = create_app()

# Reflect the changes in the database
with app.app_context():
    db.create_all()