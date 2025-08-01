from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    return HttpResponse('This is the home page')

def register(request):
    return HttpResponse('This is the registration page')
