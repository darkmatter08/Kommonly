from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from organizer.models import *
from organizer.forms import *
from sponsor.models import *
from sponsor.forms import *
from events.forms import *

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def organizer_signup(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	
	organizerForm = UserSignUpForm(request.POST)
	if organizerForm.is_valid():
		fname = organizerForm.cleaned_data['first_name']
		lname = organizerForm.cleaned_data['last_name']
		password  = organizerForm.cleaned_data['password']
		email = organizerForm.cleaned_data['email']
		organization = organizerForm.cleaned_data['organization']
		user = User.objects.create_user(first_name=fname, last_name=lname, username=email, email=email, password=password)
		user.backend='django.contrib.auth.backends.ModelBackend' 
		Organizer.objects.create(user=user, organization=organization)
		
		# Log them in and redirect after creating their user object
		return login_helper(request, organizerForm.cleaned_data['email'], organizerForm.cleaned_data['password'])
	return HttpResponseRedirect('/')

def organizer_login(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	
	organizerForm = UserLoginForm(request.POST)
	if organizerForm.is_valid():
		# Log them in and redirect
		return login_helper(request, organizerForm.cleaned_data['email'], organizerForm.cleaned_data['password'])
	else:
		return HttpResponseRedirect('/')

# Method that handles login via Django auth system
def login_helper(request, username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
			return HttpResponseRedirect('/organizer/home')
		else:
			# TODO: add in an error page - try logging in again
			return HttpResponseRedirect('/')
	else:
		#TODO: Return an 'invalid login' error message.
		return HttpResponseRedirect('/')
	
@login_required
def organizer_home(request):
	currentOrganizer = Organizer.objects.get(user=request.user)
	events = Event.objects.filter(organizer=currentOrganizer)
	context = { 'request': request, "organizer": currentOrganizer, "events": events}
	return render(request, 'organizer/organizer_dashboard.html', context)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
