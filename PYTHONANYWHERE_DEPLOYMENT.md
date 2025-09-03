# PythonAnywhere Deployment Guide

## Step 1: Create PythonAnywhere Account

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Create a free beginner account

## Step 2: Set Up Web App

1. Go to "Web" tab in dashboard
2. Click "Add a new web app"
3. Choose "Manual configuration" (Django)
4. Select Python version 3.10

## Step 3: Environment Variables

In Web app configuration, add these environment variables:
SECRET_KEY=your-production-secret-key-change-this
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
PYTHONANYWHERE_DATABASE_NAME=yourusername$default
PYTHONANYWHERE_DATABASE_USER=yourusername
PYTHONANYWHERE_DATABASE_PASSWORD=your-database-password
PYTHONANYWHERE_DATABASE_HOST=yourusername.mysql.pythonanywhere-services.com

text

## Step 4: Database Setup

1. Go to "Databases" tab
2. Create MySQL database
3. Note database name, username, and password

## Step 5: Upload Code

1. Go to "Files" tab
2. Upload your project files or clone from GitHub
3. Set up virtual environment: `python -m venv venv`
4. Install requirements: `pip install -r requirements.txt`

## Step 6: Final Setup

1. Run migrations: `python manage.py migrate`
2. Collect static files: `python manage.py collectstatic`
3. Reload web app from "Web" tab

## Step 7: Create Superuser

1. Go to "Consoles" tab
2. Start bash console in your project directory
3. Run: `python manage.py createsuperuser`
