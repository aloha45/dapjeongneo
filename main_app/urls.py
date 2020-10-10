from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dreams/', views.dreams_index, name='index')
]