from django.db import models, migrations
from datetime import date
from django.urls import reverse

# Create your models here.


class Dream(models.Model):
    title = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dream_id': self.id})
