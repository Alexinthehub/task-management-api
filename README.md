# TaskFlow Backend – The Engine Behind Your Task Management

![TaskFlow Logo](https://via.placeholder.com/800x200/0f172a/ffffff?text=TaskFlow+Backend)

This is the **backend API** that powers TaskFlow – a task management application designed to help individuals and teams organise their work, track progress, and collaborate seamlessly.

While the frontend is what you see and click, the backend is the **brain** that stores your data, handles user logins, sends email reminders, and processes every action you take in the app.

---

## 📋 What This Backend Does (In Plain English)

| What You Do in the App    | What the Backend Does                                                             |
| ------------------------- | --------------------------------------------------------------------------------- |
| **Sign up / Log in**      | Securely creates your account and manages your session using JWT tokens.          |
| **Create a task**         | Saves your task details (title, due date, priority, etc.) to the database.        |
| **Lock a task**           | Encrypts your lock password and stores it safely; only you can unlock it.         |
| **Share a task**          | Generates a unique, time‑limited link that anyone can use to view the task.       |
| **Receive notifications** | Checks for upcoming due dates and sends you email reminders.                      |
| **View analytics**        | Aggregates your tasks by status, priority, and category to show you visual stats. |
| **Manage your profile**   | Updates your avatar, nickname, and password securely.                             |

---

## 🧠 How It All Fits Together

```mermaid
graph LR
    A[Frontend React App] --> B[TaskFlow Backend API]
    B --> C[(Database)]
    B --> D[Email Service]
    B --> E[File Storage for Avatars]
(Diagram placeholder – you can add a real one later using mermaid or an image.)

🛠️ Technology Stack
Layer	Technology
Framework	Django 5.2 + Django REST Framework
Authentication	JWT (via rest_framework_simplejwt)
Database	SQLite (development) / MySQL (production on PythonAnywhere)
Email	SMTP (Gmail) / SendGrid
Task Scheduling	Django management commands (cron / Celery optional)
File Uploads	Pillow for image processing
API Documentation	DRF Spectacular (OpenAPI / Swagger)
Deployment	PythonAnywhere
🗂️ Key Data Models
Model	Purpose
User	Stores user credentials and profile info.
Profile	Extends User with avatar, nickname.
Task	Main task entity – title, description, due date, priority, status, lock, favourite, pin.
Category	Labels for grouping tasks (many‑to‑many with Task).
Notification	Unread notifications for users.
SharedTask	Tracks shared links, their tokens, expiry, and status.

📬 Main API Endpoints
Method	Endpoint	Description
POST	/api/register/	Create a new user account.
POST	/api/login/	Obtain JWT access and refresh tokens.
POST	/api/token/refresh/	Refresh an expired access token.
GET	/api/tasks/	List all tasks for the authenticated user.
POST	/api/tasks/	Create a new task.
GET	/api/tasks/{id}/	Retrieve a single task.
PUT/PATCH	/api/tasks/{id}/	Update a task.
DELETE	/api/tasks/{id}/	Delete a task.
POST	/api/tasks/{id}/lock/	Lock a task with a password.
POST	/api/tasks/{id}/unlock/	Unlock a task.
POST	/api/tasks/{id}/toggle-favorite/	Toggle favourite status.
POST	/api/tasks/{id}/toggle-pin/	Toggle pin status.
POST	/api/tasks/{id}/duplicate/	Duplicate a task.
GET	/api/notifications/	List unread notifications.
PATCH	/api/notifications/{id}/mark-read/	Mark a notification as read.
POST	/api/notifications/mark-all-read/	Mark all notifications as read.
GET	/api/categories/	List user’s categories.
POST	/api/categories/	Create a new category.
POST	/api/share/	Generate a share link for a task.
GET	/api/share/{token}/	View a shared task (public).
GET	/api/analytics/	Get task statistics for charts.
POST	/api/change-password/	Change user password.
POST	/api/profile/delete-account/	Delete the user account.
POST	/api/feedback/	Submit user feedback (with optional screenshot).
For full interactive documentation, visit /api/docs/ (Swagger UI) when the server is running.

🚀 Getting Started (For Developers)
Prerequisites
Python 3.10+

pip

Virtual environment (recommended)

Installation
bash
# Clone the repository
git clone https://github.com/Alexinthehub/task-management-api.git
cd task-management-api

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (for admin access)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
The API will be available at http://127.0.0.1:8000/api/.

Environment Variables
Create a .env file or set these in your shell:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
FRONTEND_URL=http://localhost:5173

📁 Project Structure (Simplified)
text
task_management_api/
├── task_manager/          # Project settings & main URLs
├── tasks/                 # Task, category, share, notification logic
├── profiles/              # User profile (avatar, nickname)
├── templates/             # HTML email templates
├── static/                # Collected static files
├── media/                 # User-uploaded avatars
├── manage.py
├── requirements.txt
└── README.md

📧 Email Features
The backend sends several types of emails:

Welcome email – upon registration.

Password reset – when a user requests a reset.

Task reminder – for tasks due within 24 hours (run via cron).

Task share – when someone shares a task with you.

All emails are styled with a clean, branded HTML template.

🖼️ Screenshots (Placeholders)
Screenshots will be added once the frontend is fully complete.

Swagger API Docs	Email Example	Admin Panel
https://screenshots/swagger.png	https://screenshots/email.png	https://screenshots/admin.png
🔒 Security
JWT Authentication – all API endpoints (except login, register, public share) require a valid token.

Password hashing – uses Django’s built‑in PBKDF2.

Lock passwords – stored as hashes (never plain text).

CSRF exempt for API – the backend uses JWT, not session cookies.

🚀 Deployment
The backend is deployed on PythonAnywhere. The production configuration uses:

MySQL database (via pythonanywhere_config.py).

Environment variables for secrets.

Cron jobs for daily task reminders.

Static and media files served correctly.


📄 License
MIT License – see the LICENSE file for details.

## 📬 Contact

- **Project Link**: [https://github.com/Alexinthehub/task-management-api](https://github.com/Alexinthehub/task-management-api)
- **Live API**: [https://mwendwa.pythonanywhere.com/api/docs/](https://mwendwa.pythonanywhere.com/api/docs/)

Built with ❤️ by the TaskFlow Team
```
