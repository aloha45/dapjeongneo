from django.db import models, migrations
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Dream(models.Model):
    title = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dream_id': self.id})

class Dreamboard(models.Model):
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    home = models.BooleanField(default=False)
    atom = models.BooleanField(default=False)
    book = models.BooleanField(default=False)
    hand_holding_heart = models.BooleanField(default=False)
    seedling = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    tree = models.BooleanField(default=False)
    crow = models.BooleanField(default=False)
    cloud_rain = models.BooleanField(default=False)
    skull = models.BooleanField(default=False)
    hiking = models.BooleanField(default=False)
    pen = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Created on {self.created_date} at {self.created_time}.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dreamboard_id': self.id})