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

    def __str__(self):
        return self.video_name

class VideoLoader(models.Model):
    video = models.URLField(max_length = 200)

    def __str__(self):
        return self.video

