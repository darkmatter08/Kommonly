from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from sponsor.models import *

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
	return render(request, 'sponsor/profile.html', {'business':business, 'funding_types':sponsorship_types})
	
def contact(request, business_id):
	if request.user.is_authenticated():
		return HttpResponse("user exists")
	else:
		return HttpResponse("Login required to contact businesses")
