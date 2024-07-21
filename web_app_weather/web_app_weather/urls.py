"""Главный файл с URL."""
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('metcast.urls', namespace='metcast')),
    path('api/', include('api.urls', namespace='api')),
]
