from django.views.generic import CreateView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views import View

from .models import Weather
from .forms import WeatherForm
from .utils import get_weather_forecast


class WeatherCreateView(CreateView):
    """Представление страницы ввода города."""

    model = Weather
    form_class = WeatherForm
    template_name = 'metcast/weather_form.html'

    def post(self, request, *args, **kwargs):
        city = request.POST.get('city')
        if Weather.objects.filter(city=city).exists():
            weather = Weather.objects.get(city=city)
            weather.count_call += 1
            weather.save()
            return redirect('metcast:detail', city=weather.city)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.count_call = 1
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('metcast:detail', kwargs={'city': self.object.city})


class WeatherDetailView(DetailView):
    """Представление отдельного города и информации о погоде в нем."""

    model = Weather
    template_name = 'metcast/weather_detail.html'
    slug_field = 'city'
    slug_url_kwarg = 'city'

    def get_object(self):
        return get_object_or_404(Weather, city=self.kwargs['city'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weather_cost'] = get_weather_forecast(
            self.object.city
        )
        return context


class CityAutocomplete(View):
    """Класс для автозаполнения поля "Города"."""

    def get(self, request, *args, **kwargs):
        if 'term' in request.GET:
            qs = Weather.objects.filter(
                city__icontains=request.GET.get('term')
            )
            cities = list(qs.values_list('city', flat=True))
            return JsonResponse(cities, safe=False)
        return JsonResponse([], safe=False)
