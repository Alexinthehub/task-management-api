"""
PythonAnywhere specific configuration.
This file can be imported in settings.py for PA-specific settings.
"""
import os

# PythonAnywhere-specific settings
IS_PYTHONANYWHERE = 'PYTHONANYWHERE_DOMAIN' in os.environ

if IS_PYTHONANYWHERE:
    DEBUG = False
    ALLOWED_HOSTS = [os.environ['PYTHONANYWHERE_SITE'], '127.0.0.1']
    
    # Database configuration for PythonAnywhere
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