from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news(request):
    news = Articles.objects.all()
    return render(request, 'news.html', {'news':news})

def add(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'add.html', data)