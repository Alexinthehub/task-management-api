# tasks/tests/test_notifications.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Task, Notification
from django.utils import timezone
from datetime import timedelta

class NotificationTests(APITestCase):
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        
        # Get JWT token
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_notifications(self):
        """Test retrieving user notifications"""
        # Create a notification
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            due_date=timezone.now() + timedelta(hours=5)
        )
        Notification.objects.create(
            user=self.user,
            message='Test notification',
            related_task=task
        )
        
        url = reverse('notification-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['message'], 'Test notification')

    def test_mark_notification_as_read(self):
        """Test marking a notification as read"""
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            due_date=timezone.now() + timedelta(hours=5)
        )
        notification = Notification.objects.create(
            user=self.user,
            message='Test notification',
            related_task=task
        )
        
        url = reverse('notification-mark-read', kwargs={'pk': notification.id})
        response = self.client.patch(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Notification.objects.get(id=notification.id).read)

    def test_cannot_access_other_users_notifications(self):
        """Test users cannot access other users' notifications"""
        other_user = User.objects.create_user(
            username='otheruser', 
            password='testpass123'
        )
        
        task = Task.objects.create(user=other_user, title='Other Task')
        notification = Notification.objects.create(
            user=other_user,
            message='Other user notification',
            related_task=task
        )
        
        # Try to access other user's notification
        url = reverse('notification-mark-read', kwargs={'pk': notification.id})
        response = self.client.patch(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)