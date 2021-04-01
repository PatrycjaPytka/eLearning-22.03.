import datetime
from django.db import models
from django.utils import timezone


class Lesson(models.Model):
    lesson_name = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Data publikacji')
    
    def __str__(self):
        return self.lesson_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
    video_name = models.CharField(max_length = 200)
    video_content = models.CharField(max_length = 400, blank = True, null = True)
    video_url = models.URLField(max_length = 200, blank = True, null = True)
    video_password = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.video_name


    



