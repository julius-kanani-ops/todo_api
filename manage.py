# manage.py

import sys
from app import create_app, db
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a Flask app instance
app = create_app()

def create_tables():
    """A command to create all database tables."""
    print("Creating database tables...")
    # The 'with app.app_context()' is crucial. It sets up the
    # necessary context for SQLAlchemy to know which app it's
    # working with, and thus what the database URI is.
    with app.app_context():
        db.create_all()
    print("Database tables created successfully.")

# This part allows us to run commands from the command line.
# For example: python manage.py create_tables
if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "create_tables":
            create_tables()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Usage: python manage.py <command>")
