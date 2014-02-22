# Shawn Jain 
# 2/3/2014
# Kommonly project

# imports
from django.db import models
from django import forms

from organizer import *
from organizer.models import *
from django.contrib.auth.models import User

# class OrganizerForm(forms.ModelForm):
# 	class Meta:
# 		model = Organizer
# 		fields = ['name_user', 'email', 'password', 'organization']

class UserSignUpForm(forms.ModelForm):
	fname = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'placeholder' : 'First Name', 'style' : 'display: block;'}))
	lname = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'placeholder' : 'Last Name', 'style' : 'display: block;'}))
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(max_length = 30, widget = forms.TextInput(attrs = {'placeholder' : 'Enter name', 'style' : 'display: block;'}))
	organization = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'placeholder' : 'Organization', 'style' : 'display: block;'}))
	class Meta:
		model = User
		fields = ['fname', 'lname', 'password', 'email', 'organization' ]    	

class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(max_length = 30, widget = forms.TextInput(attrs = {'placeholder' : 'Enter name', 'style' : 'display: block;'}))
	class Meta:
		model = User
		fields = ['password', 'email' ]    	

