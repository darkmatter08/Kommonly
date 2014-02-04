from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from organizer.models import *
from organizer.forms import *

def show_dashboard(request):
	print "Hello there. This is the organizer page"
	return render(request, 'organizer/temp_home.html')

@csrf_exempt
def organizer_signup(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	organizerForm = OrganizerForm(request.POST)
	print organizerForm.is_bound
	print organizerForm.is_valid()
	print organizerForm.cleaned_data
	return HttpResponseRedirect('/organizer/home')

def organizer_home(request):
	return render(request, 'organizer/organizer_dashboard.html')