# PythonAnywhere specific settings
import os

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['PYTHONANYWHERE_DATABASE_NAME'],
        'USER': os.environ['PYTHONANYWHERE_DATABASE_USER'],
        'PASSWORD': os.environ['PYTHONANYWHERE_DATABASE_PASSWORD'],
        'HOST': os.environ['PYTHONANYWHERE_DATABASE_HOST'],
        'PORT': '3306',
    }
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = '/home/Mwendwa/task_management_api/staticfiles'

# Security settings for production
ALLOWED_HOSTS = [
    'mwendwa.pythonanywhere.com',  # ← Your actual domain
    'www.pythonanywhere.com', 
    '127.0.0.1',
    'localhost'
]
DEBUG = True 