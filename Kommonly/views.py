# Shawn Jain 
# 2/3/2014
# Kommonly project

from django.template.loader import get_template
from django.template import Context
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt
from Kommonly.models import *
from organizer.forms import * 

def home(request):
	form = OrganizerForm()
	t = get_template('temp_home.html')
	html = t.render(Context({'form': form}))
	return HttpResponse(html)