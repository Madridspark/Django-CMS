from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Column, Article

def index(request):
    context = {
        'columns' : Column.objects.all()
    }
    return render(request, 'index.html', context)

def column_detail(request, column_link):
    context = {
        'column' : Column.objects.get(link=column_link)
    }
    return render(request, 'column.html', context)

def article_detail(request, pk, article_link):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    if article_link != article.link:
        return redirect(article, permanent=True)
    return render(request, 'article.html', context)