from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

from organizer.models import *

# Create your views here.
def show_dashboard(request):
	print "Hello there. This is the organizer page"
	return render(request, 'organizer/temp_home.html')


