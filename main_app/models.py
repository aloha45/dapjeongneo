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
    one = models.BooleanField(default=False)
    two = models.BooleanField(default=False)
    three = models.BooleanField(default=False)
    four = models.BooleanField(default=False)
    five = models.BooleanField(default=False)
    six = models.BooleanField(default=False)
    seven = models.BooleanField(default=False)
    eight = models.BooleanField(default=False)
    nine = models.BooleanField(default=False)
    ten = models.BooleanField(default=False)
    eleven = models.BooleanField(default=False)
    twelve = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Created on {self.created_date} at {self.created_time}.'