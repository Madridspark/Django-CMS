# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from central.models import StaticInfo

def index(request):
    return render(request, 'branch-index.html', {'staticInfo' : StaticInfo.objects.all()[0]})