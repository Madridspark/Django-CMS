# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import StaticInfo, StaticAbout, HeroImages, Page1Video, BranchList
from django.contrib import auth
from django.contrib.auth.models import User
from statistic import counter
from django.core.mail import send_mail
from winter.settings import EMAIL_HOST_USER
from branch.models import Column, Article

def indexContext():
    return {
        'staticInfo' : StaticInfo.objects.all()[0],
        'noticeImage' : HeroImages.objects.filter(theHeroTitle='特别关注')[0],
        'videoFiles' : Page1Video.objects.all()[0]
    }

def index(request):
    counter(request)
    context = {
        'intro' : StaticAbout.objects.filter(theName='intro')[0],
        'team' : StaticAbout.objects.filter(theName='team')[0],
        'commi' : StaticAbout.objects.filter(theName='commi')[0],
        'heroImages' : HeroImages.objects.exclude(theHeroTitle='特别关注'),
        'hots' : Column.objects.all()[0].article_set.all()[:4],
        'branchs' : BranchList.objects.all(),
    }
    return render(request, 'central/index.html', dict(indexContext(), **context))


def about(request):
    counter(request)

    art = request.GET['art']
    staticTeammates = StaticAbout.objects.filter(theName=art)[0]

    context = {
        'title' : staticTeammates.theTitle,
        'content' : staticTeammates.theContent,
        'image' : staticTeammates.theImage
    }
    return render(request, 'central/about.html', dict(indexContext(), **context))


def login(request):
    counter(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect("/branch")
    context = {
        'isLoginSuccess' : True
    }
    return render(request, 'central/login.html', dict(indexContext(), **context))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    counter(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect("/branch")
    context = {
        'branchs' : BranchList.objects.all(),
        'isSignupSuccess' : True
    }
    return render(request, 'central/signup.html', dict(indexContext(), **context))

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
              
    return render(request, 'central/login.html', dict(indexContext(), **context))

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
                return render(request, 'central/signup.html', dict(indexContext(), **context))
            
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
        return render(request, 'central/signup.html', dict(indexContext(), **{}))
    
    return render(request, 'central/signup.html', dict(indexContext(), **{}))


def sendEmail(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        commi =request.POST.get('commi','')
        content = request.POST.get('content','')
        send_mail(u'【' + indexContext()['staticInfo'].theName + u'后台通知】【有事找我们】【姓名:' + name + u'】', u'联系方式:'  + commi + u'\r\n' + content, EMAIL_HOST_USER, ['1059494754@qq.com'], fail_silently=False)
        return HttpResponseRedirect("/")

    return render(request, 'central/send-email.html', dict(indexContext(), **{}))
    

def joinUs(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        commi =request.POST.get('commi','')
        send_mail(u'【' + indexContext()['staticInfo'].theName + u'后台通知】【有意加入我们】【姓名:' + name + u'】', u'联系方式:'  + commi, EMAIL_HOST_USER, ['1059494754@qq.com'], fail_silently=False)
        return HttpResponseRedirect("/")

    return render(request, 'central/join-us.html', dict(indexContext(), **{}))