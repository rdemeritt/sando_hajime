from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    fundraiser = {
    }
    return render(request, 'index.html', context=fundraiser)


def about(request):
    context = {}
    return render(request, 'about.html', context=context)
