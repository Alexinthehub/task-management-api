from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView, NotificationListView, NotificationMarkAsReadView
from django.http import JsonResponse

def tasks_root(request):
    return JsonResponse({
        'message': 'Tasks API',
        'endpoints': {
            'tasks': '/api/tasks/',
            'task_detail': '/api/tasks/{id}/',
            'notifications': '/api/notifications/',
            'mark_notification_read': '/api/notifications/{id}/mark-read/'
        }
    })

urlpatterns = [
    path('', tasks_root, name='tasks-root'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/mark-read/', NotificationMarkAsReadView.as_view(), name='notification-mark-read'),
]
