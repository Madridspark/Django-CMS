# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from central.models import StaticInfo
from models import BranchInfo, FriendlyLink, Column, Article, Post
from statistic import counter

ONE_PAGE_OF_ARTICLE = 20

baseContext = {
    'staticInfo' : StaticInfo.objects.all()[0],
    'branch' : BranchInfo.objects.all()[0],
    'columns' : Column.objects.all()[1:]
}


def index(request):
    counter(request)
    columns = Column.objects.all()[1:]

    context = {
        'hot' : Column.objects.all()[0],
        'friendly_links' : FriendlyLink.objects.all()
    }

    return render(request, 'branch/index.html', dict(baseContext, **context))

def column(request, columnId):
    return columnPage(request, columnId, 1)

def columnPage(request, columnId, page):
    counter(request)
    column = Column.objects.filter(id=columnId)[0]
    pagesCount = column.article_set.count() / ONE_PAGE_OF_ARTICLE
    temp = column.article_set.count() % ONE_PAGE_OF_ARTICLE

    if temp > 0:
        pagesCount += 1
    
    currentPage = int(page)
    
    if currentPage > pagesCount or currentPage < 1:
        currentPage = 1
    
    startPos = ONE_PAGE_OF_ARTICLE * (currentPage-1)
    endPos = startPos + ONE_PAGE_OF_ARTICLE
    dataList = column.article_set.all()[startPos : endPos]

    context = {
        'columnId' : columnId,
        'dataList' : dataList,
        'page' : currentPage,
        'pagesCount' : range(1, pagesCount+1)
    }

    return render(request, 'branch/column.html', dict(baseContext, **context))


def article(request, articleId):
    counter(request)
    context = {
        'article' : Article.objects.filter(id=articleId)[0],
    }
    return render(request, 'branch/article.html', dict(baseContext, **context))