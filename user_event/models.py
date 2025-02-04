from django.db import models

class UserEvent(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    event = models.ForeignKey('event.Event', on_delete=models.PROTECT)
    