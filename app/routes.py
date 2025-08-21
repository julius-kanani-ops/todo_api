#!/usr/bin/python3


from .models import Task
from flask import Blueprint, jsonify, abort, request
from . import db


# Create a Blueprint object
main = Blueprint('main', __name__)


# Dummy data (for now, so the app still runs before we rewrite)
tasks = [
    {'id': 1, 'title': 'buy groceries', 'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 'completed': False},
    {'id': 2, 'title': 'learn python', 'description': 'Need to find a good Python tutorial on the web', 'completed': False}
]


# Define our first API endpoint
@main.route("/", methods=["GET"])
def welcome():
    """ A welcome message to confirm the api is running."""
    return jsonify(
        {"message": "Welcome to the To-Do List API!"})

# Second API endpoint to get all tasks.
@main.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Retrieve all tasks from the database.

    This endpoint handles GET requests to `/tasks` and returns
    a JSON response containing a list of all tasks in the system.

    Returns:
        Response (flask.Response): A JSON object with the structure:
            {
                "tasks": [
                    {task_1_data},
                    {task_2_data},
                    ...
                ]
            }
    """

    all_tasks = Task.query.all()
    tasks_list = [task.to_dict() for task in all_tasks]

    return jsonify(
        {
            'tasks': tasks_list
        })


# Third API endpoint to get a single task.
@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Retrieve a single task by its ID.

    This endpoint handles GET requests to `/tasks/<task_id>` and
    returns the task details as JSON if found. If the task does not exist,
    it returns a 404 error with a descriptive message.

    Args:
        task_id (int): The unique identifier of the task.

    Returns:
        Response (flask.Response): A JSON object with the structure:
            {
                "task": {task_data}
            }

    Raises:
        404 Not Found: If no task with the given ID exists.
    """
    task = Task.query.get(task_id)
    if task is None:
        abort(404, description=f"Task with id {task_id} not found")
    return jsonify({'task': task.to_dict()})


# Fourth API endpoint to create a new task.
@main.route('/tasks', methods=['POST'])
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
@main.route('/tasks/<int:task_id>', methods=['PUT'])
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
@main.route('/tasks/<int:task_id>', methods=['DELETE'])
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

