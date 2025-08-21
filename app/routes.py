#!/usr/bin/python3


from app import app, db
from app.models import Task
from flask import jsonify, abort, request


# Dummy data (for now, so the app still runs before we rewrite)
tasks = [
    {'id': 1, 'title': 'buy groceries', 'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 'completed': False},
    {'id': 2, 'title': 'learn python', 'description': 'Need to find a good Python tutorial on the web', 'completed': False}
]


# Define our first API endpoint
@todo_app.route("/", methods=["GET"])
def welcome():
    """ A welcome message to confirm the api is running."""
    return jsonify(
        {"message": "Welcome to the To-Do List API!"})

# Second API endpoint to get all tasks.
@todo_app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(
        {
            'tasks': tasks
        })


# Third API endpoint to get a single task.
@todo_app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Find the task with the matching ID in our list.

    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0: # If no task is found, the list will be empty.
        abort(404)

    return jsonify(
        {
            'task': task[0]
        })


# Fourth API endpoint to create a new task.
@todo_app.route('/tasks', methods=['POST'])
def create_task():
    # Check if the request has json data, and if the 'title' key is missing.
    if not request.json or not 'title' in request.json:
        abort(400) # Bad Request.

    # Determine the new task's ID
    if tasks:
        new_id = tasks[-1]['id'] + 1
    else:
        new_id = 1 # If the list is empty, start with ID 1.

    # Create the new task dictionary.
    new_task = {
        'id': new_id,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'completed': False
    }

    # Add the new task to our list.
    tasks.append(new_task)

    # Return the new task along with a 201 Created Status code
    return jsonify(
        {
            'task': new_task
        }), 201


# Fifth API endpoint, to find a specific task, and update it.
@todo_app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Find the task to update.
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404) # Task not found.

    # Basic Validation of the incoming data
    if not request.json:
        abort(400, description="Request must be JSON")

    if 'title' in request.json and not isinstance(request.json['title'], str):
        abort(400, description="Title must be string.")

    if 'completed' in request.json and not isinstance(request.json['completed'], bool):
        abort(400, description="Completed must be a boolean.")

    # Update the task with the new values.
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['completed'] = request.json.get('completed', task[0]['completed'])

    # Return the updated task.
    return jsonify(
        {
            'task': task[0]
        })


# Sixth API endpoint to delete a specific task.
@todo_app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Find the task to delete
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404) # Task not found

    # Remove the task from the list
    tasks.remove(task[0])

    # Return a success message
    return jsonify(
        {
            'result': True
        })

