from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dream
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dreams_index(request):
    dreams = Dream.objects.all()
    return render(request, 'dreams/index.html', {'dreams': dreams})

def dreams_detail(request, dream_id):
    dream = Dream.objects.get(id=dream_id)
    return render(request, 'dreams/detail.html', { 'dream': dream })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render (request, 'registration/signup.html', context)

class DreamCreate(CreateView):
    model = Dream
    fields = ['title', 'mood', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DreamUpdate(UpdateView):
    model = Dream
    fields = ['mood', 'description']

class DreamDelete(DeleteView):
    model = Dream
    success_url = '/dreams/'