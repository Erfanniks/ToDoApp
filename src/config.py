# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/todolistdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ... other configuration variables
