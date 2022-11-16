from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_GET

from django.views.generic import TemplateView

# Create your views here.

# @require_GET
def index(request):
    return render(request, 'index.html')

def question(request):
    return render(request, 'question.html')

def ask(request):
    return render(request, 'ask.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')
    
def signup(request):
    return render(request, 'signup.html')

def logout(request):
    return HttpResponse("logout(((")

def error(request):
    return HttpResponse("error")