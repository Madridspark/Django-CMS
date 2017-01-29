# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import StaticInfo, StaticTeammates, HeroImages

def index(request):
    personList = StaticTeammates.objects.all()
    temp = [personList[0],]
    staticTeammates = []
    for i in range(1, len(personList)):
        if i % 3 == 0:
            staticTeammates.append(temp)
            temp = []
        temp.append(personList[i])
    else:
        staticTeammates.append(temp)

    context = {
        'staticTeammates' : staticTeammates,
        'staticInfo' : StaticInfo.objects.all()[0],
        'heroImages' : HeroImages.objects.exclude(theHeroTitle='特别关注'),
        'noticeImage' : HeroImages.objects.filter(theHeroTitle='特别关注')[0]
    }
    return render(request, 'central_index.html', context)