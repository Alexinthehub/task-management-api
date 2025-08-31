# tasks/cron.py
from datetime import datetime, timedelta
from .models import Task, Notification

def check_for_due_tasks():
    one_day_from_now = datetime.now().date() + timedelta(days=1)
    tasks_due_soon = Task.objects.filter(due_date=one_day_from_now, completed=False)

    for task in tasks_due_soon:
        # Check if a notification for this task already exists to avoid duplicates
        if not Notification.objects.filter(task=task, is_sent=False).exists():
            Notification.objects.create(
                user=task.user,
                task=task,
                message=f'Reminder: Your task "{task.title}" is due on {task.due_date.strftime("%Y-%m-%d")}.'
            )