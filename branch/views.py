# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from central.models import StaticInfo
from models import BranchInfo, FriendlyLink, Column, Article, Post, PostReply
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


def bbs(request):
    return bbsPage(request, 1)

def bbsPage(request, page):
    counter(request)
    pagesCount = Post.objects.count() / ONE_PAGE_OF_ARTICLE
    temp = Post.objects.count() % ONE_PAGE_OF_ARTICLE

    if temp > 0:
        pagesCount += 1
    
    currentPage = int(page)
    
    if currentPage > pagesCount or currentPage < 1:
        currentPage = 1
    
    startPos = ONE_PAGE_OF_ARTICLE * (currentPage-1)
    endPos = startPos + ONE_PAGE_OF_ARTICLE
    dataList = Post.objects.all()[startPos : endPos]

    context = {
        'dataList' : dataList,
        'page' : currentPage,
        'pagesCount' : range(1, pagesCount+1)
    }

    return render(request, 'branch/bbs.html', dict(baseContext, **context))

def bbsPost(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            title = request.POST.get('title','')
            content = request.POST.get('content','')
            author = request.user

            post = Post()
            post.title = title
            post.content = content
            post.author = author
            post.save()

            return HttpResponseRedirect("/branch/bbs")
    return HttpResponseRedirect("/login")

def post(request, postId):
    counter(request)
    context = {
        'post' : Post.objects.filter(id=postId)[0],
    }
    return render(request, 'branch/post.html', dict(baseContext, **context))

def postReply(request, postId):
    if request.user.is_authenticated():
        if request.method == 'POST':
            content = request.POST.get('content','')
            author = request.user

            reply = PostReply()
            reply.content = content
            reply.author = author
            reply.to = Post.objects.filter(id=postId)[0]
            reply.save()

            return HttpResponseRedirect("/branch/bbs/post/" + postId)
    return HttpResponseRedirect("/login")