from django.urls import path

from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:lesson_id>/', views.detail, name = 'detail'),
    path('<int:lesson_id>/<int:video_id>/', views.loadvideo, name = 'loadvideo'),
    path('<int:lesson_id>/<int:video_id>/pass_video/', views.pass_video, name = 'pass_video'),
]
