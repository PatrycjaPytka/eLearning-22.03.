from django.shortcuts import render, redirect
from django import template
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from welcome.forms import UserForm, UserType
from django.contrib.auth.forms import UserCreationForm

from .models import AboutUs, ContactUs, News


def contact_us(request):
    contact_us_list = ContactUs.objects.all()
    template = loader.get_template('welcome/contact.html')
    context = {
        'contact_us_list': contact_us_list,
    }
    return HttpResponse(template.render(context, request))


def about_us(request):
    about_us_list = AboutUs.objects.all()
    template = loader.get_template('welcome/about.html')
    context = {
        'about_us_list': about_us_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    news_list = News.objects.all()
    template = loader.get_template('welcome/index.html')
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context, request))


def teach_learn(request):
    template = loader.get_template('welcome/teach_learn.html')
    return HttpResponse(template.render({}, request))


def reg_user(request):
    if request.user.is_authenticated:
        return redirect('lessons:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password1'))           
            user.save()
            return redirect('welcome:login')

        else:
            return redirect('welcome:reg_user')

    else:
        form = UserCreationForm()

    return render(request, 'welcome/reg_user.html', {'form':form})


def reg_staff(request):
    if request.user.is_authenticated:
        return redirect('lessons:index')

    if request.method == 'POST':
        pl = Permission.objects.filter(codename__in = ['add_group', 'change_group', 'delete_group', 'view_group', 
                                                    'add_user', 'view_user',
                                                    'add_lesson', 'change_lesson', 'delete_lesson', 'view_lesson',
                                                    'add_video', 'change_video', 'delete_video', 'view_video',
                                                    'add_video_lesson', 'change_video_lesson', 'delete_video_lesson', 'view_video_lesson',
                                                    'add_video_loader', 'change_video_loader', 'delete_video_loader', 'view_video_loader',
                                                    'view_welcome', 'add_log_entry'])
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password1'))
            user.is_staff = True
            user.user_permissions.add(*pl)
            user.save()
            return redirect('welcome:login')
                
        else:
            return redirect('welcome:reg_staff')

    else:
        form = UserCreationForm()

    return render(request, 'welcome/reg_staff.html', {'form':form})

    
def login_user(request):
    if request.user.is_authenticated:
        return redirect('lessons:index')

    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))

            if user:
                login(request, user)
                return redirect('lessons:index')


    form = UserForm()
    return render(request, 'welcome/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('welcome:login')