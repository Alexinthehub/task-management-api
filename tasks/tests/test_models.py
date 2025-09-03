# tasks/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Task, Notification
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )

    def test_create_task(self):
        """Test creating a task"""
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test description',
            due_date=timezone.now() + timezone.timedelta(days=1)
        )
        self.assertEqual(str(task), 'Test Task')
        self.assertFalse(task.completed)

    def test_create_notification(self):
        """Test creating a notification"""
        task = Task.objects.create(user=self.user, title='Test Task')
        notification = Notification.objects.create(
            user=self.user,
            message='Test notification',
            related_task=task
        )
        self.assertIn('Test notification', str(notification))
        self.assertFalse(notification.read)