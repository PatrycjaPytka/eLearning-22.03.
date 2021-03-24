from django.contrib import admin

from .models import Lesson, Video


admin.site.register(Lesson)
admin.site.register(Video)