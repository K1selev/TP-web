from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_GET

from django.views.generic import TemplateView

# Create your views here.

# @require_GET
def index(request):
    #return HttpResponse("hello world")
    return render(request, 'index.html')


def question(request):
    # return HttpResponse("hello world")
    return render(request, 'question.html')

def ask(request):
    # return HttpResponse("hello world")
    return render(request, 'ask.html')

def profile(request):
    # return HttpResponse("hello world")
    return render(request, 'profile.html')

def login(request):
    # return HttpResponse("hello world")
    return render(request, 'login.html')
    
def signup(request):
    # return HttpResponse("hello world")
    return render(request, 'signup.html')

def logout(request):
    return HttpResponse("logout(((")
    # return render(request, 'signup.html')