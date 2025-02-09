from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment
from .forms import CommentForm


# Create your views here.
def event_list(request):
    # F
    available_event = Event.objects.all()
    
    return render(
        request,
        'event_list.html',
        context={'available_events': available_event}  
    )

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment
from .forms import CommentForm

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    comments = event.comments.all()  # Get all comments for this event
    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.event = event
                comment.user = request.user
                comment.save()
                return redirect('event_detail', pk=event.pk)  # ✅ Corrected

        else:
            return redirect('login')  # Redirect to login page

    return render(request, 'event_detail.html', {  # ✅ Ensures an HttpResponse is returned
        'event': event,
        'comments': comments,
        'form': form
    })
