# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import StaticInfo, StaticAbout, HeroImages, Page1Video
from django.contrib import auth
from django.contrib.auth.models import User

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

def login(request):
    context = {
        'isLoginSuccess' : True
    }
    return render(request, 'central/login.html', dict(indexContext, **context))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    context = {
        'isSignupSuccess' : True
    }
    return render(request, 'central/signup.html', dict(indexContext, **context))

def loginCommit(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    if request.method == 'POST':
        username = request.POST.get('name','')
        password = request.POST.get('password','')

        user= auth.authenticate(username=username,password=password)
        
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/")

    context = {
        'isLoginSuccess' : False
    }
              
    return render(request, 'central/login.html', dict(indexContext, **context))

def signupCommit(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    try:
        if request.method=='POST':
            username = request.POST.get('name','')
            password =request.POST.get('password','')
            email = request.POST.get('email','')

            if User.objects.filter(username = username).count() > 0:
                context = {
                    'isSignupSuccess' : False,
                    'username' : username,
                    'email' : email
                }
                return render(request, 'central/signup.html', dict(indexContext, **context))
            
            user = User()
            user.username = username
            user.set_password(password)
            user.email = email
            user.save()
            info = StaticInfo.objects.all()[0]
            print info.theSigners
            info.theSigners += 1
            info.save()

            # #用户扩展信息 profile
            # profile=UserProfile()
            # profile.user_id=user.id
            # profile.phone=phone
            # profile.save()
            # 登录前需要先验证

            newUser = auth.authenticate(username = username,password = password)
            if newUser:
                auth.login(request, newUser)#g*******************
                return HttpResponseRedirect("/")
    except Exception,e:
        return render(request, 'central/signup.html', dict(indexContext, **{}))
    
    return render(request, 'central/signup.html', dict(indexContext, **{}))