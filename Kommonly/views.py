from django.template.loader import get_template
from django.template import *
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404

from organizer.forms import * 

def home(request):
	# form = OrganizerForm()
	return render(request, 'homepage.html')
