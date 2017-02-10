# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import StaticInfo, StaticAbout, HeroImages, Page1Video

indexContext = {
    'staticInfo' : StaticInfo.objects.all()[0],
    'noticeImage' : HeroImages.objects.filter(theHeroTitle='特别关注')[0],
    'videoFiles' : Page1Video.objects.all()[0]
}

def index(request):
    context = {
        'intro' : StaticAbout.objects.filter(theTitle='网站简介')[0],
        'team' : StaticAbout.objects.filter(theTitle='管理团队')[0],
        'heroImages' : HeroImages.objects.exclude(theHeroTitle='特别关注')
    }
    return render(request, 'central/index.html', dict(indexContext, **context))

def team(request):
    staticTeammates = StaticAbout.objects.filter(theTitle='管理团队')[0]

    context = {
        'content' : staticTeammates.theContent,
        'image' : staticTeammates.theImage
    }
    return render(request, 'central/team.html', dict(indexContext, **context))

def about(request):
    staticTeammates = StaticAbout.objects.filter(theTitle='网站简介')[0]

    context = {
        'content' : staticTeammates.theContent,
        'image' : staticTeammates.theImage
    }
    return render(request, 'central/about.html', dict(indexContext, **context))