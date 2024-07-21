from django.db import models
from django.urls import reverse


class Weather(models.Model):
    city = models.CharField(max_length=100,
                            unique=True,
                            blank=False,
                            null=False
                            )
    count_call = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse('metcast:detail', kwargs={'city': self.city})

    def __str__(self):
        return self.city
