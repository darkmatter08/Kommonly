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
        fname = organizerForm.cleaned_data['fname']
        lname = organizerForm.cleaned_data['lname']
        password  = organizerForm.cleaned_data['password']
        email = organizerForm.cleaned_data['email']
        organization = organizerForm.cleaned_data['organization']
        user = User.objects.create_user(first_name=fname, last_name=lname, username=email, email=email, password=password)
        user.backend='django.contrib.auth.backends.ModelBackend' 
        Organizer.objects.create(user=user, organization=organization)
        # Check their validity
        user = authenticate(username=email, password=password)
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

    return HttpResponseRedirect('/')


def organizer_login(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    organizerForm = UserLoginForm(request.POST)
    if organizerForm.is_valid():

        username = request.POST['email']
        password = request.POST['password']
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
    else:
        return HttpResponseRedirect('/')
    
@login_required
def organizer_home(request):
    currentOrganizer = Organizer.objects.get(user=request.user)
    events = Event.objects.filter(organizer=currentOrganizer)
    context = { 'request': request, "organizer": currentOrganizer, "events": events}
    return render(request, 'organizer/organizer_dashboard.html', context)

@csrf_exempt
def newEvent(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    currentOrganizer = Organizer.objects.get(user=request.user)
    eventForm = EventForm(request.POST, options=Sponsor_types.objects.all())
    
    if eventForm.is_valid():

        newEvent = Event(organizer=currentOrganizer, event_date=eventForm.cleaned_data['event_date'],
                         name=eventForm.cleaned_data['name'], description=eventForm.cleaned_data['description'],
                         expected_reach=eventForm.cleaned_data['expected_reach'])
        newEvent.save()
        for key in request.POST:
                try:    
                    pk = int(key)
                    stype = Sponsor_types.objects.get(pk=pk)
                    val = request.POST[key]  
                    print "VAL IS " + val
                    if val:
                        Event_Sponsorship_Preferences.objects.create(event=newEvent, sponsorship_type=stype)
                except ValueError:
                    continue
        return HttpResponseRedirect('/organizer/home')
    else:
        context = { "organizer": currentOrganizer, "newEvent": eventForm}
        return render(request, 'events/create.html', context)
    # TODO return as JSON so the client can update the page dynamically.
    # or have the client do an AJAX to get the data and update the table automatically
    #return HttpResponse(json.dumps(eventForm.cleaned_data), content_type="application/json")

# Need to be sent the event ID to look it up.
# def editEvent(request):
#     if request.method != 'POST':
#         return HttpResponseBadRequest()
#     currentOrganizer = Organizer.objects.get(user=request.user)
#     eventForm = EventForm(request.POST)
#     return HttpResponse("Under Construction")

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

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
