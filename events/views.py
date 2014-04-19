from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from organizer.models import * 
from events.models import *
from events.forms import *
from sponsor.models import *
# Create your views here.
def event_profile(request, event_id):
    currentEvent = Event.objects.get(pk=event_id)
    pictures_objects = Event_Image.objects.filter(event=currentEvent)
    picture = "/static/assets/event_image_filler.jpg"
    if len(pictures_objects) != 0:
        picture = "/static/assets/" + pictures_objects[0].pic.url.split("/")[-1]
    preferences = []
    eventSponsorshipPreferences = Event_Sponsorship_Preferences.objects.filter(event=currentEvent)
    for pref in eventSponsorshipPreferences:
        preferences.append(pref.sponsorship_type.funding_type)
    return render(request, 'events/profile.html', {"currentEvent": currentEvent, "picture_url": picture, "funding_types": preferences})

@login_required
def create_event(request):    
    return create_event_helper(request)

# Handles rendering of create event with any eventForm passed to it (for error handling)
def create_event_helper(request, eventForm=EventForm()):
    currentOrganizer = Organizer.objects.get(user=request.user)
    context = { "newEvent": eventForm, "edit": False, "sponsor_types": EventForm.getEventSponsorTypes()}
    render(request, 'events/create.html', context)
    return render(request, 'events/create.html', context)

def new_Event(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    currentOrganizer = Organizer.objects.get(user=request.user)
    eventForm = EventForm(request.POST)
    # valid_form = eventForm.is_valid()
    form_has_errors = eventForm.errors
    # if not valid_form:
    if form_has_errors:
        print "form has errors"*10
        return create_event_helper(request, eventForm=eventForm)
    return edit_or_update_event(request, currentOrganizer, Event(organizer=currentOrganizer))

# Edit Event
@login_required
def edit_event(request, event_id):
    currentEvent = Event.objects.get(pk=event_id)
    currentOrganizer = Organizer.objects.get(user=request.user)

    oldEventForm = EventForm(request.POST)

    # Getting the edit_event page
    if request.method == 'GET' or not oldEventForm.is_valid():
        eventData = { "name": currentEvent.name, "event_date": currentEvent.event_date, "expected_reach": currentEvent.expected_reach, "description": currentEvent.description, "location": currentEvent.location, "funding_sought": currentEvent.funding_sought}
        eventForm = EventForm(eventData)
        
        pictures_objects = Event_Image.objects.filter(event=currentEvent)
        picture = "/static/assets/event_image_filler.jpg"
        if len(pictures_objects) != 0:
            picture = "/static/assets/" + pictures_objects[0].pic.url.split("/")[-1]

        # form contains errors, render the oldEventForm.
        if not oldEventForm.is_valid():
            eventForm = oldEventForm
        
        context = { "newEvent": eventForm, "edit": True, "sponsor_types": EventForm.getEventSponsorTypes(currentEvent), "currentEvent": currentEvent, "picture_url": picture}
        return render(request, 'events/create.html', context)

    # Updating the event
    else:
        return edit_or_update_event(request, currentOrganizer, currentEvent)
    

# TODO Throws error if not logged in; "Could not import organizer.views.signup. View does not exist in module organizer.views.""
@login_required
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    currentOrganizer = Organizer.objects.get(user=request.user)
    if event.organizer_id == currentOrganizer.id:
        event.delete()
        return HttpResponseRedirect('/organizer/home')
    else:
        return HttpResponseRedirect('/organizer/home')

def edit_or_update_event(request, organizer, currentEvent):
    eventForm = EventForm(request.POST)
    if eventForm.is_valid():
        currentEvent.event_date = eventForm.cleaned_data['event_date']
        currentEvent.name = eventForm.cleaned_data['name']
        currentEvent.description = eventForm.cleaned_data['description']
        currentEvent.expected_reach = eventForm.cleaned_data['expected_reach']
        currentEvent.location = eventForm.cleaned_data['location']
        currentEvent.funding_sought = eventForm.cleaned_data['funding_sought']
        currentEvent.save()
    imageForm = ImageUploadForm(request.POST, request.FILES)
    if imageForm.is_valid():
        obj, created = Event_Image.objects.get_or_create(event = currentEvent, defaults = {'pic': imageForm.cleaned_data['image']})
        if not created:
            setattr(obj, 'pic', imageForm.cleaned_data['image'])
            obj.save()
    # Checkboxes are only in request.POST if they are checked ("ON"), otherwise 
    # they are not included in the request.POST. As a result, we delete all the 
    # existing preferences and create new ones
    Event_Sponsorship_Preferences.objects.filter(event=currentEvent).delete()
    for sponsorship_type in EventForm.getSponsorTypes():
        # Used dictionary.get() to get a default value in case of a failure to find. 
        # Not sure why this is entirely requried; should be in the post request no matter what 
        if request.POST.get(sponsorship_type, False): 
            stype = Sponsor_types.objects.get(funding_type=sponsorship_type)
            Event_Sponsorship_Preferences.objects.create(event=currentEvent, sponsorship_type=stype)
    return HttpResponseRedirect('/organizer/home')

