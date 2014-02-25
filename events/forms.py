# Shawn Jain 
# 2/22/2014
# Kommonly project

# imports
from django.db import models
from django import forms
from events.models import *
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['event_date', 'name', 'description']
