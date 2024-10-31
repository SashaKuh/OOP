from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('add', views.add, name='add'),
]