#routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from .database import db
from .models import Todo

main = Blueprint('main', __name__)  # Define the Blueprint


@main.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@main.route("/add", methods=["POST"])
def add():
    todo_task = request.form['todo']
    new_todo = Todo(task=todo_task, done=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/edit/<int:todo_id>", methods=["POST", "GET"])
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.task = request.form['todo']
        todo.done = 'done' in request.form
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("edit.html", todo=todo)

@main.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/done/<int:todo_id>")
def done(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.done = not todo.done  # Toggle the 'done' status
    db.session.commit()
    return redirect(url_for("main.index"))
