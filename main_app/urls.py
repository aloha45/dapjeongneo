from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dreams/', views.dream_index, name='index')
]