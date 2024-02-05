from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mail import Mail
from flask_socketio import SocketIO

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
jwt = JWTManager()
mail = Mail() 
socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True

    # Configure your database connection here
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dating_site'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '9a9690f365a7578368a141f5f9e93b5003c57a5033d46b028aae6f11a7d050c1'  # Replace with your actual secret key
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)  # Set the remember me duration
    app.config['JWT_SECRET_KEY'] = 'bdf74660b14464aee8feed7562771142f1d91af48d8f360e5cbf48317d6d81fa'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'mrteks2022@gmail.com'
    app.config['MAIL_PASSWORD']= 'pkja yaba rurg hflq'
    app.config['MAIL_DEFAULT_SENDER'] = 'mrteks2022@gmail.com'

    db.init_app(app)
    bcrypt.init_app(app)  # Initialize bcrypt with the app
    login_manager.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)
    
    # Import and register blueprints
    from app.routes.auth import auth_blueprint
    from app.routes.profile import profile_blueprint
    from app.routes.matches_routes import matches_blueprint
    from app.routes.messages_routes import messages_blueprint
    from app.routes.virtual_gifts_routes import virtual_gifts_blueprint
    from app.routes.icebreakers_routes import icebreakers_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(profile_blueprint, url_prefix='/profile')
    app.register_blueprint(matches_blueprint, url_prefix='/matches')
    app.register_blueprint(messages_blueprint, url_prefix='/messages')
    app.register_blueprint(virtual_gifts_blueprint, url_prefix='/virtual_gifts')
    app.register_blueprint(icebreakers_blueprint, url_prefix='/icebreakers')

    # Import models for SQLAlchemy
    from app.models.user import Users
    from app.models.messages import Messages
    from app.models.virtual_gifts import VirtualGifts
    from app.models.icebreakers import Icebreakers

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app