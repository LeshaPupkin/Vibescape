from django.db import models


# Create your models here.
class Description(models.Model):
    event = models.ForeignKey(
        'event.Event', 
        on_delete=models.PROTECT,
        related_name='contents',
        help_text='Event associated with the description'
        )
    title = models.CharField(max_length=80)


class Content(models.Model):
    description = models.ForeignKey(
        Description,
        on_delete=models.PROTECT,
        related_name='contents',
        help_text='Event associated with the content'
    )
    text = models.TextField(help_text='Content text')
    document = models.FileField(upload_to='documents/', help_text='Content document')   

    