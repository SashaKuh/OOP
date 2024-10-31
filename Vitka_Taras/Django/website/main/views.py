from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'main/movie_list.html', {'movies': movies})

def movie_create_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'main/movie_form.html', {'form': form})

def movie_edit_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'main/movie_form.html', {'form': form})

def home_view(request):
    movies = Movie.objects.all()  
    return render(request, 'main/movie_list.html', {'movies': movies}) 

def movie_delete_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')  
    return render(request, 'main/movie_confirm_delete.html', {'movie': movie})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

def movie_detail_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'main/movie_detail.html', {'movie': movie})