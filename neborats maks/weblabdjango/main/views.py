from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})

def another(request):
    return render(request, 'another.html')

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm()

    return render(request, 'add.html', {'form': form})