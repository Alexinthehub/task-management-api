# tasks/urls.py

from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    # This path matches the base /api/tasks/ URL for creating a task
    path('', TaskListCreateAPIView.as_view(), name='task-list-create'),
    
    # This path matches a specific task by its ID, e.g., /api/tasks/1/
    path('<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]