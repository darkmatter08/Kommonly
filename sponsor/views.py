from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from sponsor.models import *
from organizer.models import *
from django.core.mail import send_mail
from django import forms
from events.models import *

def show_business_dashboard(request):
	print "Hello there. This is the organizer page"
	return render(request, 'sponsor/dashboard.html')

def businesses(request):
	all_businesses = Organization.objects.order_by('id')
	template = loader.get_template('sponsor/index.html')
	context = RequestContext(request, {
		'all_businesses': all_businesses,
	})
	return HttpResponse(template.render(context))

def business_profile(request, business_id):
	try:
		business = Organization.objects.get(id=business_id)
		funding_types = Sponsor_types_organization.objects.filter(organization_id=business_id)
		sponsorship_types = []
		for type in funding_types:
			sponsorship_types.append(Sponsor_types.objects.get(id=type.funding_type_id).funding_type)
	except Organization.DoesNotExist:
		raise Http404
	name = "<your name>"
	eventdate = "<event date>"
	eventname = "<event name>"
	if request.user.is_authenticated():
		name = request.user.first_name 
		event = None
		if len(Event.objects.filter(organizer_id=request.user.id)) > 0:
			eventdate = Event.objects.filter(organizer_id=request.user.id)[0].event_date
			eventname = Event.objects.filter(organizer_id=request.user.id)[0].name
		
	message = "Dear " + business.contact_fname + ', I am ' + name + ' and am putting on an event on ' + eventdate + " called " + eventname + ". We would love to have you sponsor our organization with either money, food, swag or possibly a venue. In exchange, our organization, " + Organizer.objects.get(user_id=request.user.id).organization + ", will..."
	data = {'subject': business.name + " sponsorship for event", 'message':message,'organizer_email':request.user.email}
	return render(request, 'sponsor/profile.html', {'business':business, 'funding_types':sponsorship_types, 'organizer':request.user, 'form':ContactForm(data)})

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, initial="Sponsorship for ")
    message = forms.CharField()
    organizer_email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

def contact(request, business_id):
	if not request.user.is_authenticated():
		return HttpResponse("Please login to contact businesses")
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			send_mail(request.POST['subject'], request.POST['message'], request.POST['organizer_email'],
    ['team@kommonly.com'], fail_silently=False)
			return HttpResponse('thanks')
	
	business = Sponsor.objects.get(id=business_id)
	return HttpResponse('thanks')
