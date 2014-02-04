# Shawn Jain 
# 2/3/2014
# Kommonly project

# imports
from django.db import models
from django import forms

from organizer import *
from organizer.models import *

class OrganizerForm(forms.ModelForm):
	class Meta:
		model = Organizer
		fields = ['name_user', 'email', 'password', 'organization']
