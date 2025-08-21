#!/usr/bin/python3


from app import create_app, db
from app.models import Task
from dotenv import load_dotenv


load_dotenv() # Load variables from .env


app = create_app()


# This is a useful Flask feature that lets you create a shell context
# to work with your app and database directly from the terminal.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Task': Task}

if __name__ == "__main__":
    app.run(debug=True)
