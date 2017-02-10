# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from central.models import StaticInfo
from models import Column, Article


baseContext = {
    'staticInfo' : StaticInfo.objects.all()[0],
    'branch' :{ 'name' : "长安大学"},
    'hot' : Column.objects.all()[0],
    'columns' : Column.objects.all()[1::]
}
def index(request):
    context = {}

    return render(request, 'branch/index.html', dict(baseContext, **context))