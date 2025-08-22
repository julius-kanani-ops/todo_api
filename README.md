# To-Do List REST API

A complete and production-ready REST API for managing a simple to-do list. This project was built from scratch using Python, Flask, and SQLAlchemy, following modern software engineering best practices. It is designed to be a robust backend service for any front-end application (web, mobile, etc.).

The live API is deployed on Render and can be accessed at: [todo-api](https://todo-api-qabf.onrender.com/)

---

## Core Features

*   **Full CRUD Functionality:** Create, Read, Update, and Delete to-do tasks.
*   **RESTful Architecture:** Follows REST principles with standard HTTP methods and status codes.
*   **Persistent Data:** Uses a PostgreSQL database (in production) and SQLite (for local development) to ensure data is never lost.
*   **Production-Ready:** Served via a Gunicorn WSGI server and includes a robust database migration system with Flask-Migrate.
*   **Well-Structured:** Built using the Application Factory pattern and Blueprints for clean, scalable, and maintainable code.
*   **Dependency Management:** All dependencies are managed in a `requirements.txt` file.

---

## API Endpoints

The base URL for the API is the live deployment URL mentioned above.

| Method | Endpoint | Description | Request Body (JSON) | Success Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/tasks` | Retrieve a list of all tasks. | (None) | `200 OK` |
| `GET` | `/tasks/<id>` | Retrieve a single task by its ID. | (None) | `200 OK` |
| `POST` | `/tasks` | Create a new task. `title` is required. | `{ "title": "string", "description": "string" }` | `201 Created` |
| `PUT` | `/tasks/<id>` | Update an existing task. | `{ "title": "string", "description": "string", "completed": boolean }` | `200 OK` |
| `DELETE` | `/tasks/<id>` | Delete a task. | (None) | `200 OK` |

#### Example `POST` Request Body:
```json
{
    "title": "Learn how to write a README",
    "description": "Practice using Markdown for project documentation."
}
```

# Technology Stack

- **Backend:** Python 3.12
- **Framework:** Flask
- **Database ORM:** SQLAlchemy
- **Database Migrations:** Flask-Migrate (Alembic)
- **Database:** PostgreSQL (Production), SQLite (Development)
- **WSGI Server:** Gunicorn
- **Deployment:** Render

---

# Local Development Setup

Follow these steps to set up and run the project on your local machine.

## Prerequisites
- Python 3.8+
- Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/julius-kanani-ops/todo_api.git
cd todo_api
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

*   **Create the environment:**
    ```bash
    python -m venv venv
    ```

*   **Activate the environment:**
    *   On macOS/Linux: `source venv/bin/activate`
    *   On Windows: `venv\Scripts\activate`

### 3. Install Dependencies

Install all the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure the Environment

The application uses a `.env` file for local configuration.

*   Create a file named `.env` in the project root.
*   Add the following line to it. This tells the app to use a local SQLite database file.

    ```
    DATABASE_URL="sqlite:///tasks.db"
    ```

### 5. Set Up the Database

Run the database migrations to create your local `tasks.db` file and the `task` table.

*   First, set the `FLASK_APP` environment variable:
    *   On macOS/Linux: `export FLASK_APP=wsgi.py`
    *   On Windows: `set FLASK_APP=wsgi.py`

*   Now, run the database upgrade command:
    ```bash
    flask db upgrade
    ```
### 6. Run the Application

You can now start the local development server.

```bash
python run.py
```

The API will be running at `http://127.0.0.1:5000`. You can now use a tool like [Postman](https://www.postman.com/) to interact with your local API endpoints.
