from django.db import models
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80),
    description = models.TextField(), 
    date = models.DateTimeField(),
    location = models.CharField(max_length=100),



