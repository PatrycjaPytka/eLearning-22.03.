from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Lesson, Video, VideoLoader


def index(request):
    latest_lesson_list = Lesson.objects.order_by('-pub_date')[:5]
    template = loader.get_template('lessons/index.html')
    context = {
        'latest_lesson_list': latest_lesson_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, lesson_id):
    video_list = Video.objects.all()
    template2 = loader.get_template('lessons/detail.html')
    context = {
        'video_list': video_list,
    }
    return HttpResponse(template2.render(context, request))

def loadvideo(request, lesson_id):
    video = VideoLoader.objects.all()
    template3 = loader.get_template('lessons/loadvideo.html')
    context = {
        'video': video,
    }
    return HttpResponse(template3.render(context, request))
