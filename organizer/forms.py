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
	first_name = forms.CharField(max_length = 30, label ="", widget = forms.TextInput(attrs = {'placeholder' : 'First Name', 'style' : 'display: block;'}))
	last_name = forms.CharField(max_length = 30, label ="", widget = forms.TextInput(attrs = {'placeholder' : 'Last Name', 'style' : 'display: block;'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder' : 'Password', 'style' : 'display: block;'}), label ="",)
	email = forms.EmailField(max_length = 30,label ="", widget = forms.TextInput(attrs = {'placeholder' : 'Email', 'style' : 'display: block;'}))
	organization = forms.CharField(max_length = 30, label ="", widget = forms.TextInput(attrs = {'placeholder' : 'Organization', 'style' : 'display: block;'}))
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'password', 'email', 'organization' ]    	

class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder' : 'Password', 'style' : 'display: block;'}), label="")
	email = forms.EmailField(max_length = 30, label="", widget = forms.TextInput(attrs = {'label': None, 'help_text': "", 'placeholder' : 'Enter E-mail', 'style' : 'display: block;'}))
	class Meta:
		model = User
		fields = ['email', 'password']    	

