from django.shortcuts import render,get_object_or_404

from django.shortcuts import  render, redirect


# Create your views here.

def index(request):
    context = {}
    return render(request, 'users/index.html',)

def login(request):
    context = {}
    return render(request, 'users/login.html',)

def profile(request):
    context = {}
    return render(request, 'users/profile.html',)
def upload(request):
    context = {}
    return render(request, 'users/upload.html',)
def logout(request):
    context = {}
    return render(request, 'users/logout.html',)


