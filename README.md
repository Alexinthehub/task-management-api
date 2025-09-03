# Task Management API

A Django REST Framework backend API for managing tasks with user authentication and notifications.

## 🚀 Current Features

- **JWT Authentication** - User registration/login with secure tokens
- **Task CRUD Operations** - Create, read, update, and delete tasks
- **User-specific Data** - Users can only access their own tasks
- **Notification System** - Database model for task reminders
- **RESTful API** - Clean JSON API endpoints

## 📋 API Endpoints

### Authentication

- `POST /api/register/` - Create new user account
- `POST /api/login/` - Login and get JWT tokens
- `POST /api/token/refresh/` - Refresh access token

### Tasks (Authentication Required)

- `GET /api/tasks/` - List all tasks for current user
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/<id>/` - Get specific task
- `PUT /api/tasks/<id>/` - Update a task
- `DELETE /api/tasks/<id>/` - Delete a task

### Notifications (Authentication Required)

- `GET /api/notifications/` - List unread notifications
- `PATCH /api/notifications/<id>/read/` - Mark notification as read

## 🛠️ Installation

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd task_management_api
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   Database setup
   ```

bash
python manage.py migrate
python manage.py createsuperuser # Optional
Run server

bash
python manage.py runserver
🔐 Authentication
Use JWT tokens for authenticated endpoints:

Register: POST /api/register/ with {username, email, password}

Login: POST /api/login/ with {username, password}

Use the returned access token in headers:

text
Authorization: Bearer <your-token>
🚧 In Progress
Celery scheduled tasks for notifications

API documentation with Swagger

Deployment configuration

Comprehensive testing

📝 License
MIT License - see LICENSE file for details.

text

### **Why this approach is better right now:**

1. **Accurate**: Only includes what you've actually built
2. **Professional**: Clean and well-organized
3. **Maintainable**: Easy to update as you progress
4. **Useful**: Provides essential information for anyone viewing your project

### **What to do:**

1. **Copy this content** into your `README.md` file
2. **Replace** `<your-repo-url>` with your actual GitHub URL
3. **Commit and push**:
   ```bash
   git add README.md
   git commit -m "docs: Add initial project README with current features"
   git push origin main
   ```

## 🚀 Deployment

### PythonAnywhere Deployment

This project is configured for easy deployment on PythonAnywhere.

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com/)
2. **Follow the guide**: [PYTHONANYWHERE_DEPLOYMENT.md](PYTHONANYWHERE_DEPLOYMENT.md)
3. **Set environment variables** in web app configuration
4. **Upload code** and reload web app

See detailed instructions in [PYTHONANYWHERE_DEPLOYMENT.md](PYTHONANYWHERE_DEPLOYMENT.md).
