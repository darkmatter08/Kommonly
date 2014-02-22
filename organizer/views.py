from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from organizer.models import *
from organizer.forms import *
from sponsor.models import *
from sponsor.forms import *
from events.forms import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def show_dashboard(request):
    print "Hello there. This is the organizer page"
    return render(request, 'organizer/temp_home.html')

def organizer_signup(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    organizerForm = UserSignUpForm(request.POST)
    if organizerForm.is_valid():
        fname = organizerForm.cleaned_data['fname']
        lname = organizerForm.cleaned_data['lname']
        password  = organizerForm.cleaned_data['password']
        email = organizerForm.cleaned_data['email']
        organization = organizerForm.cleaned_data['organization']
        user = User.objects.create_user(first_name=fname, last_name=lname, username=email, email=email, password=password)
        user.backend='django.contrib.auth.backends.ModelBackend' 
        Organizer.objects.create(user=user, organization=organization)
        # Check their validity
        user = authenticate(username=username, password=password)
        print user
        print "IM HERE - new signup"
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/organizer/home')
            # TODO: add in an error page - try logging in again
            else:
                return HttpResponseRedirect('/')
        else:
            #TODO: Return an 'invalid login' error message.
            return HttpResponseRedirect('/')

    return HttpResponseRedirect('/organizer/home')


def organizer_login(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    organizerForm = UserLoginForm(request.POST)
    if organizerForm.is_valid():

        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        print "IM HERE"
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
    allEvents = Event.objects.all()
    eventTemplateVar = []
    if len(allEvents) != 0:
        for myEvent in allEvents:
            picture = Event_Image.objects.filter(event=myEvent)
            eventDict = {"name": myEvent.name, "date": myEvent.create_date, "description": myEvent.description}
            if len(picture) != 0:
                eventDict["picture"] = "/static/assets/" + picture[0].pic.url.split("/")[-1]
            eventTemplateVar.append(eventDict)
    context = { "organizer": currentOrganizer, "events": eventTemplateVar, "newEvent": EventForm()}
    return render(request, 'organizer/organizer_dashboard.html', context)

# POST request, AJAX method.
@csrf_exempt
def newEvent(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    currentOrganizer = Organizer.objects.get(user=request.user)
    eventForm = EventForm(request.POST)
    if eventForm.is_valid():
        # TODO change the organizer to the currently logged in user. 
        newEvent = Event(organizer=currentOrganizer, event_date=eventForm.cleaned_data['event_date'], name=eventForm.cleaned_data['name'], description=eventForm.cleaned_data['description'])
        newEvent.save()
        imageForm = ImageUploadForm(request.POST, request.FILES)
        if imageForm.is_valid():
            img = Event_Image.objects.create(pic=imageForm.cleaned_data['image'], event=newEvent)
            img.save()
            # return HttpResponse('image upload success')
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
