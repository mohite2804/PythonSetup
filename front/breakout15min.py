from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth



def index(request):
    return render(request, 'home/index.html')

