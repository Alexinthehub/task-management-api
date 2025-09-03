# tasks/tasks.py
from celery import shared_task
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Task, Notification

@shared_task
def check_upcoming_due_dates():
    """
    Task to check for tasks due in the next 24 hours and create notifications.
    Runs daily as a cron job.
    """
    print("Checking for upcoming due dates...")  # For debugging
    
    time_threshold = timezone.now() + timezone.timedelta(hours=24)
    upcoming_tasks = Task.objects.filter(
        due_date__lte=time_threshold,   # Due date is less than or equal to 24 hrs from now
        completed=False,                # Only incomplete tasks
    ).select_related('user')

    notifications_created = 0
    
    for task in upcoming_tasks:
        # Check if a notification already exists for this task to avoid spam
        if not Notification.objects.filter(related_task=task, read=False).exists():
            message = f'Reminder: Your task "{task.title}" is due on {task.due_date.strftime("%Y-%m-%d at %H:%M")}.'
            
            Notification.objects.create(
                user=task.user,
                message=message,
                related_task=task
            )
            notifications_created += 1
            print(f"Created notification: {message}")  # For debugging

    return f"Created {notifications_created} notifications for upcoming tasks."