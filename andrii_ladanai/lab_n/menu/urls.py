from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('another_page', views.another_page, name='another_page'),
    path('create/', views.create_post, name='create_post'),
]