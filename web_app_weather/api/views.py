from rest_framework import viewsets

from metcast.models import Weather
from .serializers import WeatherSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    """Представление для API к модели погода.
    Укажите в параметрах запроса конкретный город для
    получения информации по определенному городу.
    """

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        if city:
            return self.queryset.filter(city=city)
        return self.queryset
