from rest_framework import serializers

from metcast.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    """Сериализатор модели Weather."""

    class Meta:
        model = Weather
        fields = ('city', 'count_call', )
        read_only_fields = ('city', 'count_call', )
