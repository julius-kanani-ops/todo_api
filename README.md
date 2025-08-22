# To-Do List REST API

A complete and production-ready REST API for managing a simple to-do list. This project was built from scratch using Python, Flask, and SQLAlchemy, following modern software engineering best practices. It is designed to be a robust backend service for any front-end application (web, mobile, etc.).

The live API is deployed on Render and can be accessed at: `https://todo-api-qabf.onrender.com/`

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
