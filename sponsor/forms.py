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
	print "ContactForm"
	def __init__(self, userid, *args, **kwargs):
		print "userid", userid
		super(ContactForm, self).__init__(*args, **kwargs)
		if len(Event.objects.filter(organizer_id=13)) > 0:
			self.fields['events'] = forms.ModelChoiceField(queryset=Event.objects.filter(organizer_id=13),to_field_name="id") 

	subject = forms.CharField(max_length=100, initial="Sponsorship for ")
	message = forms.CharField(widget = forms.Textarea)
	#organizer_email = forms.EmailField()
	#if len(Event.objects.filter(organizer_id=user.id)) > 0:
		#events = forms.ModelChoiceField(queryset=Event.objects.filter(organizer_id=user.id)) 

	cc_myself = forms.BooleanField(required=False)
