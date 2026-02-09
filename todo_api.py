# Basically this file consists of the functions ..
# Functions that uses json file to read and write todos

# There are 6 functions ...
""" load_todo -  This function reads the todo list from the JSON File
    save_todo - Saves a list of todos to a JSON file.
    add_todo - adds a new todo into the json file.
    update_todo - Updates the task description of an existing to-do.
    toggle_todo - Toggle done/ not done 
    delete_todo - deletes a todo from the lost
"""

import json
import os

def load_todo(filepath):
    try:
        with open(filepath,'r') as f:
            data = json.load(f)
            return data
    
    except (json.JSONDecodeError, FileNotFoundError ):
        return []

def save_todo(filepath, todos):
    with open(filepath, 'w') as f:
        json.dump(todos, f, indent = 4)

def add_todo(filepath, task):
    todos = load_todo(filepath)
    new_id = 1

    if todos:
        new_id = max(t.get('id', 0) for t in todos) + 1
    
    new_todo = {
        'id' : new_id,
        'task' : task,
        'completed' : False
    }
    todos.append(new_todo)
    save_todo(filepath, todos)

def update_todo(filepath, todo_id, new_task):
    todos = load_todo(filepath)
    for todo in todos:
        if todo.get('id') == todo_id :
            todo['task'] = new_task
            break
    save_todo(filepath,todos)

def toggle_todo (filepath, todo_id):
    todos = load_todo(filepath)
    for todo in todos:
        if todo.get('id') == todo_id:
            todo['completed'] = not todo['completed']
            break
    save_todo(filepath,todos)

def delete_todo(filepath, todo_id):
    todos = load_todo(filepath)
    for todo in todos:
        if todo.get('id') == todo_id:
            todos.remove(todo)
            break
    save_todo(filepath,todos)


    