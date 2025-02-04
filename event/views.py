from django.shortcuts import render
from .models import Event

# Create your views here.
def event_list(request):
    # Fetch available courses that the user has not enrolled in
    available_event = Event.objects.exclude(user_events__user=request.user)
    
    return render(
        request,
        'event_list.html',
        context={'available_events': available_event}  # Use the correct context variable
    )
