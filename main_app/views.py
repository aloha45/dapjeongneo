from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Dream

# Create your views here.


# class Dream:
#     def __init__(self, title, mood, description):
#         self.title = title
#         self.mood = mood
#         self.description = description
        

# dreams = [
#     Dream('a scary dream', 'freaky', 'big scary werewolf'),
#     Dream('a nice dream', 'happy and warm', 'field in summer at dusk, barefeet in grass'),
#     Dream('kind of sexy', 'schwing', 'like a nerdy professor in hot pajamas')
# ]

def home(request):
    return render(request, 'home.html')

def dreams_index(request):
    dreams = Dream.objects.all()
    return render(request, 'dreams/index.html', {'dreams': dreams})

class DreamCreate(CreateView):
    model = Dream
    fields = ['title', 'mood', 'description']
    success_url = '/dreams/'