from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required

from app.models import Profile, Tag, Question, Answer
from app.forms import LoginForm, RegisterForm, ProfileForm, AskForm, AnswerForm

def paginate(object_list, request):
    paginator = Paginator(list(object_list), 10)
    page = request.GET.get('page')
    try:
        objects_page = paginator.get_page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return objects_page

context = {
    'popular_tags': Tag.objects.popular(),
    'best_members': Profile.objects.best(),
}

def index(request):
    newest_questions = Question.objects.newest()
    context['questions'] = paginate(newest_questions, request)
    return render(request, 'index.html', context)

def hot(request):
    hottest_questions = Question.objects.hottest()
    context['questions'] = paginate(hottest_questions, request)
    return render(request, 'hot.html', context)

def tag(request, tag_name):
    questions_by_tag = Question.objects.by_tag(tag_name)
    context['questions'] = paginate(questions_by_tag, request)
    context['tag_name'] = tag_name
    return render(request, 'tag.html', context)

def question(request, qid):
    context['question'] = Question.objects.get(pk=qid)
    form = AnswerForm(request.POST)

    if request.POST:
        if form.is_valid():
            answer = Answer.objects.create(
                question=context['question'],
                text=form.cleaned_data.get('textarea'),
                author=request.user.profile
            )
    
    context['answers'] = Answer.objects.hottest(qid)
    context['form'] = form
    return render(request, 'question.html', context)

def login(request):
    # print(request.GET)
    # print(request.POST)
    redirected_path = request.GET.get('next', '/')
    form = LoginForm(request.POST)

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse("index"))
            else:
                form.add_error(None, 'Wrong login or password')

    context['form'] = form
    return render(request, 'login.html', context)

def signup(request):
    form = RegisterForm(request.POST)

    if request.POST:
        if form.is_valid():
            name = form.cleaned_data.get('login')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            rep_password = form.cleaned_data.get('rep_password')
            if password != rep_password:
                form.add_error(None, 'Wrong repeated password')
            elif Profile.objects.is_exist(name, email):
                form.add_error(None, 'This login is already used')
            else:
                user = User.objects.create_user(name, email, password)
                profile = Profile.objects.create(user=user)
                auth.login(request, user)
                return redirect('/')

    context['form'] = form
    return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    redirected_path = request.GET.get('next', '/')
    return redirect(redirected_path)

def profile(request):
    data = {'login': request.user.username, 'email': request.user.email}
    form = ProfileForm(data, initial=data)
    
    if request.POST:
        form = ProfileForm(request.POST, initial=data)
        if form.is_valid() and form.has_changed():
            request.user.username=form.cleaned_data.get('login')
            request.user.email=form.cleaned_data.get('email')
            request.user.save()
            return redirect('/')

    context['form'] = form
    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def ask(request):
    form = AskForm(request.POST)

    if request.POST:
        if form.is_valid():
            tags = form.cleaned_data.get('tags')
            if tags:
                tags = tags.split()
                Tag.objects.create_from_list(tags)
                
            question = Question.objects.create(
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                author=request.user.profile
            )
            question.add_tags(tags)
            return redirect(reverse('question', args=[question.id]))

    context['form'] = form
    return render(request, 'ask.html', context)
