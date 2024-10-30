from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('another/', views.another, name='another'),
    path('create/', views.add, name='add'),
]