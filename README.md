# Task Management API

A Django REST Framework API for task management with user authentication, notifications, and full CRUD operations.

## 🚀 Live Deployment

**API Documentation:** https://mwendwa.pythonanywhere.com/api/docs/

## 📋 Features

- **User Authentication** (JWT tokens)
- **Task Management** (Full CRUD operations)
- **Real-time Notifications**
- **RESTful API Design**
- **Auto-generated Documentation** (Swagger/ReDoc)
- **Production-ready Configuration**

## 🔌 API Endpoints

### Authentication

- `POST /api/login/` - User login
- `POST /api/register/` - User registration
- `POST /api/token/refresh/` - Refresh JWT tokens

### Tasks

- `GET /api/tasks/` - List all tasks for authenticated user
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT /api/tasks/{id}/` - Update a task
- `PATCH /api/tasks/{id}/` - Partial task update
- `DELETE /api/tasks/{id}/` - Delete a task

### Notifications

- `GET /api/notifications/` - List unread notifications
- `PATCH /api/notifications/{id}/mark-read/` - Mark notification as read

## 🛠️ Technology Stack

- **Backend:** Django 4.2+ & Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (Development) / MySQL (Production)
- **Documentation:** DRF Spectacular (Swagger/OpenAPI)
- **Deployment:** PythonAnywhere
- **Python:** 3.10+

## 📦 Installation

1. **Clone repository**
   ```bash
   git clone <your-repo-url>
   cd task_management_api
   Create virtual environment
   ```

bash
python -m venv venv
source venv/bin/activate # Linux/Mac

# or

venv\Scripts\activate # Windows
Install dependencies

bash
pip install -r requirements.txt
Database setup

bash
python manage.py migrate
Create superuser

bash
python manage.py createsuperuser
Run development server

bash
python manage.py runserver
🚀 Deployment
This API is deployed on PythonAnywhere with:

Production settings (DEBUG=False, secure headers)

MySQL database configuration

Static files collected and served

WSGI configuration optimized

Environment Configuration
Create pythonanywhere_config.py for production:

python

# Production settings for PythonAnywhere

DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']
SECRET_KEY = 'your-production-secret-key'

# Security settings

CSRF_TRUSTED_ORIGINS = [
'https://yourusername.pythonanywhere.com',
'https://*.pythonanywhere.com',
]
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
📝 API Usage Examples
User Registration
bash
curl -X POST https://mwendwa.pythonanywhere.com/api/register/ \
 -H "Content-Type: application/json" \
 -d '{"username": "testuser", "password": "testpass123", "email": "test@example.com"}'
User Login
bash
curl -X POST https://mwendwa.pythonanywhere.com/api/login/ \
 -H "Content-Type: application/json" \
 -d '{"username": "testuser", "password": "testpass123"}'
Create Task (with JWT token)
bash
curl -X POST https://mwendwa.pythonanywhere.com/api/tasks/ \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer YOUR_JWT_TOKEN" \
 -d '{"title": "Complete API documentation", "description": "Update README and API docs", "due_date": "2023-12-31"}'
🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see LICENSE file for details.

🆘 Support
For support or questions:

Check the API documentation: https://mwendwa.pythonanywhere.com/api/docs/

Open an issue on GitHub

Contact the development team

Note: This API is currently deployed and operational. All endpoints are functional and tested.
EOL

text

Let me also show you the updated README:

```bash
cat README.md
```
