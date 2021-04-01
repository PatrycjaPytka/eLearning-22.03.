from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import Lesson, Video


def index(request):
    latest_lesson_list = Lesson.objects.order_by('-pub_date')[:5]
    template = loader.get_template('lessons/index.html')
    context = {
        'latest_lesson_list': latest_lesson_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, lesson_id):
    video_list = Video.objects.filter(lesson__pk = lesson_id)
    template2 = loader.get_template('lessons/detail.html')
    context = {
        'video_list': video_list,
    }
    return HttpResponse(template2.render(context, request))

def pass_video(request, video_id, lesson_id):
    video_lesson = Video.objects.filter(pk = video_id)
    video_list = Video.objects.filter(lesson__pk = lesson_id)
    template3 = loader.get_template('lessons/pass_video.html')
    context = {
        'video_lesson': video_lesson,
        'video_list': video_list,
    }
    return HttpResponse(template3.render(context, request))


def loadvideo(request, lesson_id, video_id):
    video_lesson = Video.objects.filter(pk = video_id)
    video_list = Video.objects.filter(lesson__pk = lesson_id)
    template3 = loader.get_template('lessons/loadvideo.html')
    context = {
        'video_lesson': video_lesson,
        'video_list': video_list,
    }
    return HttpResponse(template3.render(context, request))
