from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dream, Dreamboard
from .forms import DreamboardForm
# from .time import dclock
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import time
import datetime

boop = time.ctime()

x = boop.split()

y = x[3]

z = y.split(':')

hours = int(z[0])
minutes = int(z[1])
seconds = int(z[2])

dtime = 0

on = False

# def dclock():
#     # global seconds, minutes, hours
#     global dtime, seconds, minutes,hours
#     while on == True:
#         seconds = seconds + 1
#         time.sleep(1)
#         # dclock()
#         if seconds == 60:
#             seconds = 0
#             minutes = minutes + 1
#         if minutes == 60:
#             minutes = 0
#             hours = hours + 1
#         if hours > 12:
#             hours = hours - 12
#         dtime = (str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
#         return dtime

def dclock():
    global dtime
    while True:
        time.sleep(1)
        current_date = str(datetime.datetime.today())
        current_time = current_date.split()[1]
        basic_time = (current_time.split(':'))
        hours = basic_time[0]
        minutes = basic_time[1]
        seconds = round(float(basic_time[2]))
        dtime = (str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
        return dtime

# Create your views here.


def home(request):
    global on
    on = True
    dclock()
    return render(request, 'home.html', {'dtime': dtime })

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

@login_required
def dreamboard_create(request):
    dreamboard_form = DreamboardForm(request.POST)
    if dreamboard_form.is_valid():
        new_dreamboard = dreamboard_form.save(commit=False)
        new_dreamboard.save()
    return render (request, 'dreamboards/create.html', {
        'dreamboard_form': dreamboard_form
    })

@login_required
def dreamboards_index(request):
    dreamboards = Dreamboard.objects.filter(user=request.user)
    return render(request, 'dreamboards/index.html', { 'dreamboards': dreamboards })

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

class DreamboardCreate(CreateView):
    model = Dreamboard
    fields = ['home', 'atom', 'book', 'hand_holding_heart', 'seedling', 'music', 'tree', 'crow', 'cloud_rain', 'skull', 'hiking', 'pen']
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)