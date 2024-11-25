from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('second/', views.second_page, name='second_page'),
    path('add-article/', views.add_article, name='add_article'),
    path('edit-article/<int:article_id>/', views.edit_article, name='edit_article'),
] 