from django.urls import path

from . import views

app_name = 'welcome'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_user, name = 'login'),
    path('register/', views.registration, name = 'register'),
    path('logout/', views.user_logout, name = 'logout'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('contact/', views.contact_us, name = 'contact')
    ]