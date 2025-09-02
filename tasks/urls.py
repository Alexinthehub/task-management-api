# tasks/urls.py
from django.urls import path
from . import views
from .views import RegisterView  # Import the registration view

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    
    # Task endpoints
    path('tasks/', views.TaskListCreateAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailAPIView.as_view(), name='task-detail'),
    
    # Notification endpoints
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/read/', views.NotificationMarkAsReadView.as_view(), name='notification-mark-read'),
]