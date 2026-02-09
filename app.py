import os
from flask import Flask, render_template, request, jsonify
from todo_api import load_todo, add_todo, toggle_todo, delete_todo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'todos.json')

app = Flask(__name__)

@app.route('/')
def index():
    todos = load_todo(JSON_FILE)
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    task = data.get('task')

    if task:
        add_todo(JSON_FILE, task)
        todos = load_todo(JSON_FILE)
        return jsonify(todos[-1])  # return newly added todo

    return jsonify({"error": "Task required"}), 400


@app.route('/toggle/<int:todo_id>', methods=['PUT'])
def toggle(todo_id):
    toggle_todo(JSON_FILE, todo_id)
    todos = load_todo(JSON_FILE)

    updated = next((t for t in todos if t["id"] == todo_id), None)
    return jsonify(updated)


@app.route('/delete/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    delete_todo(JSON_FILE, todo_id)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
