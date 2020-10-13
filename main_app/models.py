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
    one = models.BooleanField()
    two = models.BooleanField()
    three = models.BooleanField()
    four = models.BooleanField()
    five = models.BooleanField()
    six = models.BooleanField()
    seven = models.BooleanField()
    eight = models.BooleanField()
    nine = models.BooleanField()
    ten = models.BooleanField()
    eleven = models.BooleanField()
    twelve = models.BooleanField()