# Shawn Jain
# 2/3/2014
# Sponsor forms

# imports
from django.db import models
from django import forms
from events.models import *

# from sponsor import *
from sponsor.models import *

class ContactForm(forms.Form):
	def __init__(self, userid, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		if len(Event.objects.filter(organizer_id=userid)) > 0:
			self.fields['events'] = forms.ModelChoiceField(queryset=Event.objects.filter(organizer_id=userid),to_field_name="id") 

	subject = forms.CharField(max_length=150)
	message = forms.CharField(widget = forms.Textarea)
	cc_myself = forms.BooleanField(required=False)
