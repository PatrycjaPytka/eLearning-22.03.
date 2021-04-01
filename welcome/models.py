import datetime
from django.db import models
from django.utils import timezone

class AboutUs(models.Model):
    text_about = models.TextField()
    name = models.CharField(max_length = 200, blank = True, null = True)
    pub_date = models.DateTimeField('Data publikacji')

    def __str__(self):
        return self.text_about

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class ContactUs(models.Model):
    email = models.EmailField(max_length = 200, blank = True, null = True)
    city = models.CharField(max_length = 100, blank = True, null = True)
    street = models.CharField(max_length = 100, blank = True, null = True) 
    country = models.CharField(max_length = 100, blank = True, null = True) 
    
    def __str__(self):
        return self.email    

class News(models.Model):
    news_name = models.CharField(max_length = 100)
    news_text = models.TextField()
    pub_date = models.DateTimeField('Data publikacji')

    def __str__(self):
        return self.news_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
