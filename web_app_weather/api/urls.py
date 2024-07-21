from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CitiesViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'weather', CitiesViewSet, basename='weather')

urlpatterns = [
    path('', include(router.urls)),
]
