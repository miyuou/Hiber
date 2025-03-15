from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
     path('/listhotel', views.list_filtre, name='list_filtre'),
]