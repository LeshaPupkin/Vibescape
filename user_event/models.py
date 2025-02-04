from django.db import models

class UserEvent(models.Model):
    user = models.ForeignKey(
        'user.User', 
        on_delete=models.PROTECT,
        related_name='user_events',
        help_text='User associated with the course'
        )
    
    event = models.ForeignKey(
        'event.Event', 
        on_delete=models.PROTECT,
        related_name='user_events',
        help_text='Course associated with the user')
    


    
class Meta:
    unique_together = (
        ('user', 'event')
        )