from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Dream

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dream_index(request):
    dreams = Dream.objects.all()
    return render(request, 'dream/index.html', {'dreams': dreams})