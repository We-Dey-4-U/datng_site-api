# app/services/authentication.py

from flask_bcrypt import Bcrypt
from flask_login import login_user as flask_login_user
from sqlalchemy.exc import IntegrityError
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from app.models.user import Users
from app.models.profile import Profiles
from app import db, mail  # Assuming you have Flask-Mail configured

bcrypt = Bcrypt()
# Secret key for token generation,
SECRET_KEY = 'your_secret_key'

# Create a URLSafeTimedSerializer instance
serializer = URLSafeTimedSerializer(SECRET_KEY)

def register_user(username, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    new_user = Users(username=username, email=email, password_hash=hashed_password)
    
    db_session = db.session
    try:
        db_session.add(new_user)
        db_session.commit()

        # Create a profile for the registered user
        new_profile = Profiles(user=new_user)
        db_session.add(new_profile)
        db_session.commit()

        # Generate and send a registration token to the user's email
        send_registration_token(new_user)

        # Automatically log in the user after successful registration
        flask_login_user(new_user, remember=False)

    except IntegrityError:
        db_session.rollback()
        raise ValueError("Username or email already exists")

def login_user(username, password, remember=False):
    user = db.session.query(Users).filter(Users.username == username).first()

    if user and bcrypt.check_password_hash(user.password_hash, password):
        # Set the user as authenticated
        user.authenticated = True
        flask_login_user(user, remember=remember)
        return user

    return None

# Function to send a registration token to the user's email
def send_registration_token(user):
    # Generate a registration token (you can use your own method to generate a token)
    registration_token = generate_registration_token(user)

    # Send the token to the user's email
    send_email(user.email, 'Registration Token', f'Your registration token: {registration_token}')

# Function to generate a registration token (you can replace it with your own token generation logic)
def generate_registration_token(user):
    # Generate a token with the user's ID
    token = serializer.dumps(user.user_id, salt='registration-salt')
    return token

# Function to send an email
def send_email(to, subject, body):
    # Use Flask-Mail to send emails
    message = Message(subject=subject, recipients=[to], body=body)
    mail.send(message)