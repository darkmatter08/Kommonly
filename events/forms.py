# Shawn Jain 
# 2/22/2014
# Kommonly project

# imports
from django.db import models
from django import forms
from events.models import *
from sponsor.models import *
from django.forms import ModelForm, Textarea

class ImageUploadForm(forms.Form):
	"""Image upload form."""
	image = forms.ImageField(label='Event Image')

class EventForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		expected_reach = forms.CharField(widget = forms.Textarea)

	class Meta:
		model = Event
		fields = ['name', 'event_date', 'expected_reach', 'description']
		widgets = {
			'expected_reach': Textarea(attrs={'cols': 80, 'rows': 10}),
		}

	## METHODS FOR SPONSORSHIP PREFERENCES: 

	# Returns a list of all the funding types
	@staticmethod
	def getSponsorTypes():
		return [ sponsor_type.funding_type for sponsor_type in Sponsor_types.objects.all() ]

	# Returns a dictionary of funding types to selection
	@staticmethod
	def getEventSponsorTypes(event=None):
		preferences = {}
		for sponsor_type in EventForm.getSponsorTypes():
			preferences[sponsor_type] = False
		if event is not None:
			eventSponsorshipPreferences = Event_Sponsorship_Preferences.objects.filter(event=event)
			for selected_sponsor_type in eventSponsorshipPreferences:
				preferences[selected_sponsor_type.sponsorship_type.funding_type] = True
		return preferences

# class Event_Sponsorship_PreferencesForm(forms.Form):
# 	# sponsorship_type_choices_inv = dict(Sponsor_types.objects.all())
# 	for item in Sponsor_types.objects.all():
# 		exec(item.funding_type + " = forms.BooleanField(required=False)")
		# exec(item.funding_type + "_desc = forms.CharField(required=False)")
	# sponsorship_type_choices = {v:k for k, v in sponsorship_type_choices_inv.items()}
	# sponsorship_type_choices["Funds"]
	# funds = forms.BooleanField(required=False)

