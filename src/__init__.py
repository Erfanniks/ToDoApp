# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__, static_folder='../static', template_folder='../templates')


# Load configurations from the config.py file
app.config.from_object('src.config.Config')

# Initialize the SQLAlchemy object
# This will be used in the models.py file for database operations
db = SQLAlchemy(app)

# Import routes
# This import is at the bottom to avoid circular dependencies
# as routes.py will need to import the 'app' variable
from src import routes
