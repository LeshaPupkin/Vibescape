from django.contrib import admin
from .models import Event



class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id','title','description','location','duration')

admin.site.register(Event)

