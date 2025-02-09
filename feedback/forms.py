# feedback/forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['event', 'comment']  # You can include 'event' if you want to select it
