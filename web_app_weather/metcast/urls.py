from django.urls import path

from . import views
from .views import CityAutocomplete

app_name = 'metcast'

urlpatterns = [
    path('', views.WeatherCreateView.as_view(),
         name='create'),
    path('detail/<str:city>/',
         views.WeatherDetailView.as_view(),
         name='detail'),
    path('city-autocomplete/',
         CityAutocomplete.as_view(),
         name='city-autocomplete'),
]
