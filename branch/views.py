# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'branch-index.html', context)