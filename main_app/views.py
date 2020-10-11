from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dream

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dreams_index(request):
    dreams = Dream.objects.all()
    return render(request, 'dreams/index.html', {'dreams': dreams})

def dreams_detail(request, dream_id):
    dream = Dream.objects.get(id=dream_id)
    return render(request, 'dreams/detail.html', { 'dream': dream })

class DreamCreate(CreateView):
    model = Dream
    fields = ['title', 'mood', 'description']
    success_url = '/dreams/'

class DreamUpdate(UpdateView):
    model = Dream
    fields = ['mood', 'description']

class DreamDelete(DeleteView):
    model = Dream
    success_url = '/dreams/'