# app/models.py
from app import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.task}>'
