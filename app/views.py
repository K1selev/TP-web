from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from app.models import *
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# @require_GET
def index(request):
    return render(request, 'index.html')

def paginate(objects_list, request, per_page=6):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page=per_page)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def question(request):
    return render(request, 'question.html')

# попытался добавить контекст

    # try:
    #     question = Question.objects.get(pk=id)
    # except Exception:
    #     return HttpResponseNotFound("ERROR 404: NOT FOUND")

    # question = Question.objects.get(pk=id)
    # answers = question.answers.all()
    # paged_obj = paginate(objects_list=answers, request=request)
    # context = {'question': question,
    #            'answers': paged_obj,
    #            'paged_obj': paged_obj}
    # return render(request, 'question.html', context=context)

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