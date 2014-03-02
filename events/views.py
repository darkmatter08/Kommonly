from django.shortcuts import render
from organizer.models import * 
from events.models import *
from events.forms import *
# Create your views here.
def create_event(request):
    return event_view(request=request)

def event_view(request=None, eventForm=EventForm(), Event_Sponsorship_PreferencesForm=Event_Sponsorship_PreferencesForm()):
    currentOrganizer = Organizer.objects.get(user=request.user)
    context = { "organizer": currentOrganizer, "newEvent": eventForm, "newEvent_Sponsorship_PreferencesForm": Event_Sponsorship_PreferencesForm}
    return render(request, 'events/create.html', context)

def edit_event(request, event_id):
    currentEvent = Event.objects.get(pk=event_id)
    eventData = { "name": currentEvent.name, "event_date": currentEvent.event_date, "expected_reach": currentEvent.expected_reach, "description": currentEvent.description}
    eventForm = EventForm(eventData)
    # preferencesForm = Event_Sponsorship_PreferencesForm(preferencesData)
    return event_view(request=request, eventForm=eventForm)
