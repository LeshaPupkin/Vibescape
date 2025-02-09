from django.shortcuts import render

# Create your views here.
# feedback/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Set the user to the currently logged-in user
            feedback.save()
            return redirect('success_page')  # Redirect to a success page or the event page
    else:
        form = FeedbackForm()

    return render(request, 'submit_feedback.html', {'form': form})
