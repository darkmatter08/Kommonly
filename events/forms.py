# Shawn Jain 
# 2/22/2014
# Kommonly project

# imports
from django.db import models
from django import forms
from events.models import *
# from django.forms import *

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'event_date', 'expected_reach', 'description']

# class Event_Sponsorship_PreferencesForm(forms.ModelForm):
# 	class Meta:
# 		model = Event_Sponsorship_Preferences
# 		fields = ['sponsorship_type', 'sponsorship_amount']
# 		widgets = {
# 			'sponsorship_type': forms.CheckboxSelectMultiple()
# 		}

class Event_Sponsorship_PreferencesForm(forms.Form):
	sponsorship_type_choices_inv = dict(Event_Sponsorship_Preferences.sponsorship_type_choices)
	for number, item in Event_Sponsorship_Preferences.sponsorship_type_choices:
		exec(item + " = forms.BooleanField(required=False)")
		exec(item + "_desc = forms.CharField()")
	# sponsorship_type_choices = {v:k for k, v in sponsorship_type_choices_inv.items()}
	# sponsorship_type_choices["Funds"]
	# funds = forms.BooleanField(required=False)

