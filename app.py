from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/todolistdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model Definition
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.task}>'

# Routes
@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo_task = request.form['todo']
    new_todo = Todo(task=todo_task, done=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:todo_id>", methods=["POST", "GET"])
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.task = request.form['todo']
        todo.done = 'done' in request.form
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/done/<int:todo_id>")
def done(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.done = not todo.done  # Toggle the 'done' status
    db.session.commit()
    return redirect(url_for("index"))


# Add more routes as needed

if __name__ == "__main__":
    app.run(debug=True)
