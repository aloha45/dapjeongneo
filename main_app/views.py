from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dream
from .time import dclock
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# dclock()

def home(request):
    return render(request, 'home.html', {'time': dclock()})

@login_required
def dreams_index(request):
    dreams = Dream.objects.filter(user=request.user)
    return render(request, 'dreams/index.html', {'dreams': dreams})

@login_required
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

class DreamCreate(LoginRequiredMixin, CreateView):
    model = Dream
    fields = ['title', 'mood', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DreamUpdate(LoginRequiredMixin, UpdateView):
    model = Dream
    fields = ['mood', 'description']

class DreamDelete(LoginRequiredMixin, DeleteView):
    model = Dream
    success_url = '/dreams/'