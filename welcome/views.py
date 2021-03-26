from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from welcome.forms import UserForm
from django.contrib.auth.forms import UserCreationForm

from .models import AboutUs, ContactUs


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
    return render(request, 'welcome/index.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('lessons:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'), email=request.POST.get('email'))
            user.save()
            return redirect('welcome:login')

        else:
            return redirect('welcome:register')

    else:
        form = UserCreationForm()
    return render(request, 'welcome/register.html', {'form':form})

    
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