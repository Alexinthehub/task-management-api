# Task Management API

### Project Description

This is a robust and scalable Task Management API built with Django and Django REST Framework. The API allows users to register, authenticate, and manage their tasks. It supports full CRUD (Create, Read, Update, Delete) functionality for tasks and includes filtering capabilities.

### Features

- **User Authentication:** Secure user registration and token-based login.
- **Task Management:** Full CRUD operations for creating, retrieving, updating, and deleting tasks.
- **Filtering:** Users can filter their task list by `status` and `priority`.
- **Private Endpoints:** All task-related endpoints are protected and require a valid authentication token.

### API Endpoints

#### User Authentication

- **Register:** `POST /api/register/`
- **Login:** `POST /api/login/`

#### Task Management

- **List Tasks:** `GET /api/tasks/`
- **Create Task:** `POST /api/tasks/`
- **Retrieve Task:** `GET /api/tasks/<id>/`
- **Update Task:** `PATCH /api/tasks/<id>/`
- **Delete Task:** `DELETE /api/tasks/<id>/`

### How to Run the Project

1.  Clone this repository to your local machine.
2.  Navigate to the project directory.
3.  Create and activate a Python virtual environment.
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run database migrations:
    ```bash
    python manage.py migrate
    ```
6.  Start the Django development server:
    `bash
    python manage.py runserver
    `
    The API will be available at `http://127.0.0.1:8000/`.

---

### How to Push the `README` File

After you have created the `README.md` file, you need to add it to your repository and push the changes to GitHub.

1.  **Stage the new file:**

    ```bash
    git add README.md
    ```

2.  **Commit your changes:**

    ```bash
    git commit -m "Add README file"
    ```

3.  **Push the changes to your remote repository:**
    ```bash
    git push origin main
    ```
