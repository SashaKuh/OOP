from django.urls import path
from .views import home_view, movie_create_view, movie_edit_view, movie_delete_view, movie_detail_view

urlpatterns = [
    path('', home_view, name='movie_list'),
    path('new/', movie_create_view, name='movie_create'),
    path('edit/<int:id>/', movie_edit_view, name='movie_edit'),
    path('delete/<int:id>/', movie_delete_view, name='movie_delete'),
    path('detail/<int:id>/', movie_detail_view, name='movie_detail'),  # Додано маршрут для деталей фільму
]
