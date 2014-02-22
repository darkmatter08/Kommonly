from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

from sponsor.models import *

# Create your views here.
# Create your views here.
def show_company_dashboard(request):
	print "Hello there. This is the organizer page"
	return render(request, 'sponsor/dashboard.html')

def get_companies(request):
	print "Companies"
	return render(request, 'sponsors')
	