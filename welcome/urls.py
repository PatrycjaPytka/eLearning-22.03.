from django.urls import path

from . import views

app_name = 'welcome'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_user, name = 'login'),
    path('reg_user/', views.reg_user, name = 'reg_user'),
    path('reg_staff/', views.reg_staff, name = 'reg_staff'),
    path('logout/', views.user_logout, name = 'logout'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('contact/', views.contact_us, name = 'contact'),
    path('teachorlearn/', views.teach_learn, name = 'teach_learn'),
    ]