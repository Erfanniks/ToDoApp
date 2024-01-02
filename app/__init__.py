# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

# Load configurations from the config.py file
app.config.from_object('config.Config')

# Initialize the SQLAlchemy object
# This will be used in the models.py file for database operations
db = SQLAlchemy(app)

# Import routes
# This import is at the bottom to avoid circular dependencies
# as routes.py will need to import the 'app' variable
from app import routes
