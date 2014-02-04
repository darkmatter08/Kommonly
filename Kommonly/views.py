# Shawn Jain 
# 2/3/2014
# Kommonly project

from django.template.loader import get_template
from django.template import *
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt
from Kommonly.models import *

def home(request):
	form = OrganizerForm()
	t = get_template('temp_home.html')
	html = t.render(RequestContext(request, {'form': form}))
	return HttpResponse(html)

# @csrf_exempt
def organizer_signup(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	organizerForm = OrganizerForm(request.POST)
	print organizerForm.is_bound
	print organizerForm.is_valid()
	print organizerForm.cleaned_data
	return HttpResponseRedirect('/organizer/home')

def organizer_home(request):
	return HttpResponse("organizer_home")
	
