from django.shortcuts import render
from organizer.models import * 
from events.models import *
from events.forms import *
# Create your views here.
def event_profile(request, event_id):
    return render(request, 'events/profile.html', {"currentEvent": Event.objects.get(pk=event_id)})

def event_view(request=None, eventForm=EventForm(), edit=False):
    currentOrganizer = Organizer.objects.get(user=request.user)
    context = { "organizer": currentOrganizer, "newEvent": eventForm, "edit": edit}
    return render(request, 'events/create.html', context)

# New Event
def create_event(request):
    return event_view(request=request)

# Edit Event
def edit_event(request, event_id):
    currentEvent = Event.objects.get(pk=event_id)
    eventData = { "name": currentEvent.name, "event_date": currentEvent.event_date, "expected_reach": currentEvent.expected_reach, "description": currentEvent.description}
    eventForm = EventForm(eventData)
    # preferencesForm = Event_Sponsorship_PreferencesForm(preferencesData)
    return event_view(request=request, eventForm=eventForm, edit=True)
