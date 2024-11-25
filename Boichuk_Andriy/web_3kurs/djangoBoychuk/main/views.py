from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'main/home.html', {'articles': articles})

def second_page(request):
    return render(request, 'main/second.html')

def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Article.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'main/add_article.html')

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            article.title = title
            article.content = content
            article.save()
            return redirect('home')
            
    return render(request, 'main/edit_article.html', {'article': article}) 