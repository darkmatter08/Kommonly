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
		'businesses': all_businesses,
	})
	return render(request, 'sponsor/all_businesses.html', context)

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
	eventreach = "<expected reach>"
	organization = "<organization>"
	email = "team+anonymous@kommonly.com"
	if request.user.is_authenticated():
		name = request.user.first_name 
		event = None
		if len(Event.objects.filter(organizer_id=request.user.id)) > 0:
			eventdate = 'EVENT DATE FOUND' #vent.objects.filter(organizer_id=request.user.id)[0].event_date
			eventname = Event.objects.filter(organizer_id=request.user.id)[0].name
			eventreach = Event.objects.filter(organizer_id=request.user.id)[0].expected_reach
			organization = Organizer.objects.get(user_id=request.user.id).organization
			email = request.user.email
		
	message = "Dear " + business.contact_fname + ', I am ' + name + ' and am putting on an event on '
	message += eventdate + " called " + eventname + ". We would love to have you sponsor our organization with "
	message += "either money, food, swag or possibly a venue. In exchange, our organization, "
	message += organization + ", will promote your brandname "
	message += "at our event, list you as a sponsor on all our marketing materials, and invite you to attend our event "
	message += "and connect with our talented students. We anticipate " + eventreach + " people to attend, most of whom would be very interested in your company. "
	message += "Sponsoring our event would show a real commitment to <STATE YOUR CAUSE HERE>, which we believe "
	message += "would reflect quite positively on your company. It will also be a lot of fun to attend if you choose to send "
	message += "members of " + business.name + " to " + eventname + "."
	data = {'subject': business.name + " sponsorship for event", 'message':message,'organizer_email':email}
	return render(request, 'sponsor/profile.html', {'business':business, 'funding_types':sponsorship_types, 'organizer':request.user, 'form':ContactForm(data)})

class ContactForm(forms.Form):
	print "contactform"
	subject = forms.CharField(max_length=100, initial="Sponsorship for ")
	message = forms.CharField(widget = forms.Textarea)
	organizer_email = forms.EmailField()
	#events = forms.ModelMultipleChoiceField(["hello", "goodbye"]]) 

	cc_myself = forms.BooleanField(required=False)

def contact(request, business_id):
	print "contact reached"
	if request.method == 'POST':
		form = ContactForm(request.POST)
		print(form)
		if form.is_valid():
			print "form is valid"
			send_mail(request.POST['subject'], request.POST['message'], request.POST['organizer_email'],
	['amymichelleyin@gmail.com'], fail_silently=False)
			return null
	
	business = Sponsor.objects.get(id=business_id)
	return
