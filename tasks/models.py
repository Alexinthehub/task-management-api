# tasks/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Add a due_date field to your existing Task model if it doesn't exist
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ADD THIS FIELD FOR THE NOTIFICATION SYSTEM TO WORK
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

# ADD THIS NEW MODEL
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    related_task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"