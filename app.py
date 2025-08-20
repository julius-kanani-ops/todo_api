from flask import Flask, jsonify


# Create a Flask application instance
todo_app = Flask(__name__)

# Define our first API endpoint
@todo_app.route("/", methods=["GET"])
def welcome():
    """ A welcome message to confirm the api is running."""
    return jsonify(
        {"message": "Welcome to the To-Do List API!"})


# This part is a god practice: it ensures the server runs only
# when the script is executed directly ( and not when imported).
if __name__ == "__main__":
    todo_app.run(debug=True)
