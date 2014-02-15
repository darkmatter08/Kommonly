from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from organizer.models import *
from organizer.forms import *
from sponsor.models import *
from sponsor.forms import *




def show_dashboard(request):
	print "Hello there. This is the organizer page"
	return render(request, 'organizer/temp_home.html')

@csrf_exempt
def organizer_signup(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	organizerForm = OrganizerForm(request.POST)
	print organizerForm.is_bound
	print organizerForm.is_valid()
	print organizerForm.cleaned_data
	return HttpResponseRedirect('/organizer/home')

def organizer_home(request):
	allEvents = Event.objects.all()
	eventTemplateVar = []
	if len(allEvents) != 0:
		for myEvent in allEvents:
			eventDict = {"name": myEvent.name, "date": myEvent.create_date, "description": myEvent.description}
			eventTemplateVar.append(eventDict)
	context = { "organizer": {"name_user": "shawn"}, "events": eventTemplateVar, "newEvent": EventForm()}
	return render(request, 'organizer/organizer_dashboard.html', context)

# POST request, AJAX method.
@csrf_exempt
def newEvent(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	eventForm = EventForm(request.POST)
	# TODO change the organizer to the currently logged in user. 
	newEvent = Event(organizer=Organizer.objects.get(email="sj@mit.edu"), event_date=eventForm.cleaned_data['event_date'], name=eventForm.cleaned_data['name'], description=eventForm.cleaned_data['description'])
	newEvent.save()
	return HttpResponseRedirect('/organizer/home')
	# TODO return as JSON so the client can update the page dynamically.
	# or have the client do an AJAX to get the data and update the table automatically
	#return HttpResponse(json.dumps(eventForm.cleaned_data), content_type="application/json")

# AJAX method to serialize all current events and return as JSON. 
# Frontend can call this to load all current events. 
@csrf_exempt
def getAllEvents(request):
	if request.method != 'POST':
		print "bad request"
		return HttpResponseBadRequest()
	allEvents = []
	for currentEvent in Event.objects.all():
		allEvents.append({"event_date" : currentEvent.event_date.strftime('%Y-%m-%dT%H:%M:%S'), "name" : currentEvent.name, "description" : currentEvent.description})
	return HttpResponse(json.dumps(allEvents), content_type="application/json")



