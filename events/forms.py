# Shawn Jain 
# 2/22/2014
# Kommonly project

# imports
from django.db import models
from django import forms
from events.models import *
from sponsor.models import *
# from django.forms import *

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class EventForm(forms.ModelForm):
	for item in Sponsor_types.objects.all():
		exec(item.funding_type + " = forms.BooleanField(required=False)")
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

# class Event_Sponsorship_PreferencesForm(forms.Form):
# 	# sponsorship_type_choices_inv = dict(Sponsor_types.objects.all())
# 	for item in Sponsor_types.objects.all():
# 		exec(item.funding_type + " = forms.BooleanField(required=False)")
		# exec(item.funding_type + "_desc = forms.CharField(required=False)")
	# sponsorship_type_choices = {v:k for k, v in sponsorship_type_choices_inv.items()}
	# sponsorship_type_choices["Funds"]
	# funds = forms.BooleanField(required=False)

