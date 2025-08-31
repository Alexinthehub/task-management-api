Task Management API
Project Description
This is a robust and scalable Task Management API built with Django and Django REST Framework. The API allows users to register, authenticate, and manage their tasks. It supports full CRUD (Create, Read, Update, Delete) functionality for tasks and includes advanced features like filtering, a notification system, and interactive API documentation.

Features
User Authentication: Secure user registration and token-based login.

Task Management: Full CRUD operations for creating, retrieving, updating, and deleting tasks.

Filtering: Users can filter their task list by status and priority.

Automated Notifications: The system sends reminders for tasks with approaching due dates via a background cron job.

API Documentation: Interactive and auto-generated API documentation is available via Swagger UI.

Private Endpoints: All task-related endpoints are protected and require a valid authentication token.

API Endpoints
User Authentication
Register: POST /api/register/

Login: POST /api/login/

Task Management
List Tasks: GET /api/tasks/

Create Task: POST /api/tasks/

Retrieve Task: GET /api/tasks/<id>/

Update Task: PATCH /api/tasks/<id>/

Delete Task: DELETE /api/tasks/<id>/

API Documentation
Swagger UI: GET /api/schema/swagger-ui/

How to Run the Project
Clone this repository to your local machine.

Navigate to the project directory.

Create and activate a Python virtual environment.

Install the required dependencies, including the new ones for this phase:

Bash

pip install -r requirements.txt
Run database migrations:

Bash

python manage.py makemigrations
python manage.py migrate
Start the Django development server:

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

How to Push the README File
After you have updated the README.md file, you need to add it to your repository and push the changes to GitHub.

Stage the file:

Bash

git add README.md
Commit your changes with a descriptive message:

Bash

git commit -m "Update README with Phase 4 features"
Push the changes to your remote repository:

Bash

git push origin main
