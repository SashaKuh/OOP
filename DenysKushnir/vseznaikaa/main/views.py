from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post  # Імпортуйте вашу модель Post

def home(request):
    posts = Post.objects.all()  # Отримання всіх постів
    return render(request, 'home.html', {'posts': posts})

def another(request):
    return render(request, 'another.html')

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігає пост в базу даних
            return redirect('home')  # Перенаправлення на домашню сторінку
    else:
        form = PostForm()

    return render(request, 'create.html', {'form': form})
