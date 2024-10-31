from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news_add', views.news_add, name='news_add'),
]