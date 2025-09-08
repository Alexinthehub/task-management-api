# Task Management API

A Django REST Framework API for task management with user authentication, notifications, and full CRUD operations.

## 🚀 Live Deployment

**API Documentation:** https://mwendwa.pythonanywhere.com/api/docs/

[![Live Deployment](https://img.shields.io/badge/PythonAnywhere-Live%20API-brightgreen)](https://mwendwa.pythonanywhere.com/api/docs/)

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

## 🖥️ Local Development

### Backend Setup
1. **Clone and setup**:
   ```bash
   git clone https://github.com/Alexinthehub/task-management-api.git
   cd task_management_api
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # or
   .venv\Scriptsctivate     # Windows
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database setup**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run development server**:
   ```bash
   python manage.py runserver
   ```
   Server runs at: http://127.0.0.1:8000/

### API Endpoints (Local)
- **API Root**: http://127.0.0.1:8000/api/
- **Documentation**: http://127.0.0.1:8000/api/docs/
- **Authentication**: http://127.0.0.1:8000/api/login/

### Frontend Development
The API accepts requests from React development server (http://localhost:3000) with CORS enabled.

## 🌐 Production Deployment
- **Live API**: https://mwendwa.pythonanywhere.com/api/
- **Live Documentation**: https://mwendwa.pythonanywhere.com/api/docs/

## 🛠️ Technology Stack

- **Backend:** Django 4.2+ & Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (Development) / MySQL (Production)
- **Documentation:** DRF Spectacular (Swagger/OpenAPI)
- **Deployment:** PythonAnywhere
- **Python:** 3.10+
