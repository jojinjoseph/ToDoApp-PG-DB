from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# PostgreSQL connection string
# Example:
# postgres://username:password@localhost:5432/dbname
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/tododb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Create Todo table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Add todo
        if "todo" in request.form:
            todo_text = request.form["todo"].strip()
            if todo_text:
                new_todo = Todo(content=todo_text)
                db.session.add(new_todo)
                db.session.commit()

        # Remove todo
        elif "remove" in request.form:
            todo_text = request.form["remove"]
            todo = Todo.query.filter_by(content=todo_text).first()
            if todo:
                db.session.delete(todo)
                db.session.commit()

        return redirect(url_for("index"))

    todolist = Todo.query.all()
    return render_template("index.html", todolist=todolist)

if __name__ == "__main__":
    app.run(debug=True)