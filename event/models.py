from django.db import models
from django.utils import timezone

from django.db import models

from django.db import models

class Event(models.Model):
    title = models.CharField(default='a', max_length=80, help_text='Event title')
    description = models.TextField(default='No description provided', help_text='Course description')  # Default for description
    location = models.CharField(default='Unknown location', max_length=100)  # Default for location
    duration = models.IntegerField(default=0)  # Default for duration


def __str__(self):     
    return self.title




