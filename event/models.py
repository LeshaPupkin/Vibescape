from django.db import models
from django.utils import timezone
from user.models import User
from django.db import models

from django.db import models

class Event(models.Model):
    title = models.CharField(default='a', max_length=80, help_text='Event title')
    description = models.TextField(default='No description provided', help_text='Course description')  # Default for description
    location = models.CharField(default='Unknown location', max_length=100)  # Default for location
    duration = models.IntegerField(default=0)  # Default for duration




class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.event}"


def __str__(self):     
    return self.title




