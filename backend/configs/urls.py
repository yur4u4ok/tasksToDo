
from django.urls import path, include

urlpatterns = [
    path('tasks', include('apps.tasks.urls')),
    path('auth', include('apps.auth.urls')),
    path("users", include('apps.users.urls')),
]
