# Shawn Jain
# 2/3/2014
# Sponsor forms

# imports
from django.db import models
from django import forms

# from sponsor import *
from sponsor.models import *
from events.models import *
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['event_date', 'name', 'description']
