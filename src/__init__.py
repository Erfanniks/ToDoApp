from flask import Flask
from .database import db  # Import db here
from .config import DATABASE_URI
from .routes import main as main_blueprint

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')


    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
