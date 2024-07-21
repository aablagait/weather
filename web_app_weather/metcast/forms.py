from django import forms

from .models import Weather


class WeatherForm(forms.ModelForm):
    """Форма для ввода города."""

    class Meta:
        model = Weather
        fields = ('city', )
