from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponseRedirect
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
    # TODO implement multiple images 
    pictures = []
    # for pic in pictures_objects:
    #     pictures.append("/static/assets/" + pic.pic.url.split("/")[-1])
    return render(request, 'events/profile.html', {"currentEvent": currentEvent, "picture_url": picture, "pictures": pictures})

def event_view(request=None, eventForm=EventForm(options=Sponsor_types.objects.all()), edit=False):
    currentOrganizer = Organizer.objects.get(user=request.user)
    context = { "organizer": currentOrganizer, "newEvent": eventForm, "edit": edit}
    return render(request, 'events/create.html', context)

# New Event
def create_event(request):    
    return event_view(request=request)

@csrf_exempt
def new_Event(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    currentOrganizer = Organizer.objects.get(user=request.user)
    eventForm = EventForm(request.POST, options=Sponsor_types.objects.all())
    print request.POST
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
        imageForm = ImageUploadForm(request.POST, request.FILES)
        if imageForm.is_valid():
            m = Event_Image.objects.create(pic=imageForm.cleaned_data['image'], event = newEvent)
            m.save()
        return HttpResponseRedirect('/organizer/home')
    else:
        context = { "organizer": currentOrganizer, "newEvent": eventForm}
        return render(request, 'events/create.html', context)
    # TODO return as JSON so the client can update the page dynamically.
    # or have the client do an AJAX to get the data and update the table automatically
    #return HttpResponse(json.dumps(eventForm.cleaned_data), content_type="application/json")

# Edit Event
def edit_event(request, event_id):
    print "IN EDIT EVENT"
    print event_id
    currentEvent = Event.objects.get(pk=event_id)
    eventData = { "name": currentEvent.name, "event_date": currentEvent.event_date, "expected_reach": currentEvent.expected_reach, "description": currentEvent.description}
    selected = Event_Sponsorship_Preferences.objects.filter(event=currentEvent)
    sarray = []
    for s in selected:
        sarray.append(str(s.sponsorship_type.id))

    print "Preferences: " + str(sarray)
    eventForm = EventForm(eventData, options=Sponsor_types.objects.all(), selected=sarray)
    print eventForm
    print eventForm.is_bound
    for i in range(1, 5):
        eventForm.fields[str(i)].initial = True
        print eventForm.fields[str(i)].initial
    # eventSponsorshipPreferences = Event_Sponsorship_Preferences.objects.filter(event=currentEvent)

    currentOrganizer = Organizer.objects.get(user=request.user)
    context = { "organizer": currentOrganizer, "newEvent": eventForm, "edit": 1}
    return render(request, 'events/create.html', context)

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    currentOrganizer = Organizer.objects.get(user=request.user)
    
    if event.organizer_id == currentOrganizer.id:
        event.delete()
        return HttpResponseRedirect('/organizer/home')
    else:

        return HttpResponseRedirect('/organizer/home')

