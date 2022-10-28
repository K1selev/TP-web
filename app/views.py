from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_GET

# Create your views here.

# @require_GET
def index(request):
    #return HttpResponse("hello world")
    return render(request, 'index.html')


def question(request):
    return HttpResponse("hello world")
    #return render(request, 'question.html')