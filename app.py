from flask import Flask, jsonify, abort, request


# Create a Flask application instance
todo_app = Flask(__name__)

# In-memory database.
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'completed': False
    },

    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'completed': False
    }
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

    # Create the new task dictionary.
    new_task = {
        'id': tasks[-1]['id'] + 1, 
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


# This part is a god practice: it ensures the server runs only
# when the script is executed directly ( and not when imported).
if __name__ == "__main__":
    todo_app.run(debug=True)
