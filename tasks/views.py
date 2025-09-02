# tasks/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, Notification
from .serializers import TaskSerializer, NotificationSerializer

# Task Views
class TaskListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all tasks and create new tasks for the authenticated user.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return tasks for the currently authenticated user
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Associate the task with the currently authenticated user
        serializer.save(user=self.request.user)

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a single task.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure a user can only access their own tasks
        return Task.objects.filter(user=self.request.user)

# Notification Views
class NotificationListView(generics.ListAPIView):
    """
    API view to list all unread notifications for the authenticated user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, read=False).order_by('-created_at')

class NotificationMarkAsReadView(generics.UpdateAPIView):
    """
    API view to mark a specific notification as read.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    http_method_names = ['patch']  # Only allow PATCH

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        # Security check: ensure the user owns the notification
        if notification.user != request.user:
            return Response({"error": "You can only mark your own notifications as read."}, status=status.HTTP_403_FORBIDDEN)
        
        notification.read = True
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)