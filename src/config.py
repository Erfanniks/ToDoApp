# config.py
import os

# Database connection parameters
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_HOST = os.environ.get('DB_HOST', 'postgres')
DB_PORT = os.environ.get('DB_PORT', '5432')  # Default port for PostgreSQL
DB_NAME = os.environ.get('DB_NAME', 'todolistdb')

# Construct the SQLALCHEMY_DATABASE_URI dynamically
DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
