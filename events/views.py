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
    currentOrganizer = Organizer.objects.get(user=request.user)
    preferences = [[1, "Venue", "id_new_1", False], [2, "Funding", "id_new_2", False], [3, "Swag", "id_new_3", False], [4, "People", "id_new_4", False]]
    context = { "organizer": currentOrganizer, "newEvent": EventForm(), "edit": False, "preferences": preferences}
    return render(request, 'events/create.html', context)

@csrf_exempt
def new_Event(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    currentOrganizer = Organizer.objects.get(user=request.user)
    return edit_or_update_event(request, currentOrganizer, Event(organizer=currentOrganizer))

# Edit Event
@login_required
def edit_event(request, event_id):
    print "IN EDIT EVENT"
    currentEvent = Event.objects.get(pk=event_id)
    currentOrganizer = Organizer.objects.get(user=request.user)

    # Updating the event
    if request.method == 'POST':
        return edit_or_update_event(request, currentOrganizer, currentEvent)

    # Getting event edit page
    else:
        print "Getting the edit event page"
        eventData = { "name": currentEvent.name, "event_date": currentEvent.event_date, "expected_reach": currentEvent.expected_reach, "description": currentEvent.description}
        selected = Event_Sponsorship_Preferences.objects.filter(event=currentEvent)
        eventForm = EventForm(eventData)
        eventSponsorshipPreferences = Event_Sponsorship_Preferences.objects.filter(event=currentEvent)
        selected = []
        for pref in eventSponsorshipPreferences:
            selected.append(pref.sponsorship_type.pk)
        
        preferences = [[1, "Venue", "id_new_1", False], [2, "Funding", "id_new_2", False], [3, "Swag", "id_new_3", False], [4, "People", "id_new_4", False]]
        for data_item in preferences: 
            if data_item[0] in selected:
                data_item[3] = True
        context = { "newEvent": eventForm, "edit": 1, "preferences": preferences, "currentEvent": currentEvent}
        return render(request, 'events/create.html', context)

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
    print "editing or updating the Event"
    eventForm = EventForm(request.POST)
    if eventForm.is_valid():
        currentEvent.event_date=eventForm.cleaned_data['event_date']
        currentEvent.name = eventForm.cleaned_data['name']
        currentEvent.description = eventForm.cleaned_data['description']
        currentEvent.expected_reach = eventForm.cleaned_data['expected_reach']
        currentEvent.save()
    else:
        context = { "organizer": organizer, "newEvent": eventForm}
        return render(request, 'events/create.html', context)
    # Checkboxes are only in request.POST if they are checked ("ON"), otherwise 
    # they are not included in the request.POST. As a result, we delete all the 
    # existing preferences and create new ones
    Event_Sponsorship_Preferences.objects.filter(event=currentEvent).delete()
    for checkboxIdOrName, sponsorship_type in EventForm.sponsorshipTypeLookup.items():
        # Used dictionary.get() to get a default value in case of a failure to find. 
        # Not sure why this is entirely requried; should be in the post request no matter what 
        if request.POST.get(checkboxIdOrName, False): 
            stype = Sponsor_types.objects.get(pk=sponsorship_type)
            Event_Sponsorship_Preferences.objects.create(event=currentEvent, sponsorship_type=stype)
    return HttpResponseRedirect('/organizer/home')