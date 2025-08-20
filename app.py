from flask import Flask, jsonify, abort


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

# This part is a god practice: it ensures the server runs only
# when the script is executed directly ( and not when imported).
if __name__ == "__main__":
    todo_app.run(debug=True)
