from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dreams/', views.dreams_index, name='index'),
    path('dreams/create/', views.DreamCreate.as_view(), name='dreams_create'),
    path('dreams/<int:dream_id>/', views.dreams_detail, name='detail'),
    path('dreams/<int:pk>/update/', views.DreamUpdate.as_view(), name='dreams_update'),
    path('dreams/<int:pk>/delete/', views.DreamDelete.as_view(), name='dreams_delete')
]