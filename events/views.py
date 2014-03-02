from django.shortcuts import render
from organizer.models import * 
from events.models import *
from events.forms import *
# Create your views here.
def create_event(request):
    # currentOrganizer = Organizer.objects.get(user=request.user)
    # allEvents = Event.objects.all()
    # eventTemplateVar = []
    # if len(allEvents) != 0:
    #     for myEvent in allEvents:
    #         picture = Event_Image.objects.filter(event=myEvent)
    #         eventDict = {"name": myEvent.name, "date": myEvent.create_date, "description": myEvent.description}
    #         if len(picture) != 0:
    #             eventDict["picture"] = "/static/assets/" + picture[0].pic.url.split("/")[-1]
    #         eventTemplateVar.append(eventDict)
    # context = { "organizer": currentOrganizer, "events": eventTemplateVar, "newEvent": EventForm(), "newEvent_Sponsorship_PreferencesForm": Event_Sponsorship_PreferencesForm()}
    # return render(request, 'events/create.html', context)
    return event_view(request=request)

def event_view(request=None, eventForm=EventForm(), Event_Sponsorship_PreferencesForm=Event_Sponsorship_PreferencesForm()):
    currentOrganizer = Organizer.objects.get(user=request.user)
    context = { "organizer": currentOrganizer, "newEvent": eventForm, "newEvent_Sponsorship_PreferencesForm": Event_Sponsorship_PreferencesForm}
    return render(request, 'events/create.html', context)

def edit_event(request, event_id):
    currentEvent = Event.objects.get(pk=event_id)
    eventData = { "name": currentEvent.name, "event_date": currentEvent.event_date, "expected_reach": currentEvent.expected_reach, "description": currentEvent.description}
    eventForm = EventForm(eventData)
    preferencesForm = Event_Sponsorship_PreferencesForm(preferencesData)
    return event_view(request=request, eventForm=eventForm)