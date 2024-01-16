from flask import Flask
from flask_migrate import Migrate
from .database import db  # Import db here
from .config import DATABASE_URI
from .routes import main as main_blueprint

migrate = Migrate()

def create_app(app=None):
    if app is None:
        app = Flask(__name__, static_folder='../static', template_folder='../templates')

    # Configure your Flask application, including the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.register_blueprint(main_blueprint)

    return app
