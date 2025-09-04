# task_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import RegisterView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication endpoints with consistent naming
    path('api/task_management_api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/task_management_api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/task_management_api/register/', RegisterView.as_view(), name='register'),
    
    # API Documentation with consistent naming
    path('api/task_management_api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/task_management_api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/task_management_api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Your app endpoints with consistent naming
    path('api/task_management_api/', include('tasks.urls')),
]