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
    """
    Create a new task.

    This endpoint handles POST requests to `/tasks` and creates
    a new task using the provided JSON payload. The payload must
    include a `title`, and can optionally include a `description`.

    Request JSON:
        {
            "title": "Task title",
            "description": "Optional task description"
        }

    Returns:
        Response (flask.Response): A JSON object with the newly
        created task and HTTP status code 201.
            {
                "task": {task_data}
            }

    Raises:
        400 Bad Request: If the request JSON is missing or the
        `title` field is not provided.
    """
    if not request.json or 'title' not in request.json:
        abort(400, description="Request must contain a title")

    new_task = Task(
        title=request.json['title'],
        description=request.json.get('description', "")
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'task': new_task.to_dict()}), 201


# Fifth API endpoint, to find a specific task, and update it.
@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Update an existing task by its ID.

    This endpoint handles PUT requests to `/tasks/<task_id>` and
    updates the specified task with the provided JSON payload.
    If the task does not exist, a 404 error is returned.

    Request JSON (partial or full):
        {
            "title": "Updated title",
            "description": "Updated description",
            "completed": true/false
        }

    Args:
        task_id (int): The unique identifier of the task to update.

    Returns:
        Response (flask.Response): A JSON object with the updated task:
            {
                "task": {task_data}
            }

    Raises:
        404 Not Found: If no task with the given ID exists.
        400 Bad Request: If the request body is missing or not JSON.
    """
    task = Task.query.get(task_id)
    if task is None:
        abort(404, description=f"Task with id {task_id} not found")
    if not request.json:
        abort(400, description="Request must be JSON")

    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.completed = request.json.get('completed', task.completed)

    db.session.commit()
    return jsonify({'task': task.to_dict()})


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

