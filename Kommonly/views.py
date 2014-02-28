# Shawn Jain 
# 2/3/2014
# Kommonly project

from django.template.loader import get_template
from django.template import *
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404

from organizer.forms import * 

from django.contrib.auth.models import User

def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/organizer/home')
	SignUpform = UserSignUpForm()
	LoginForm  = UserLoginForm()
	return render(request, 'homepage.html', {'signupForm': SignUpform, 'loginForm': LoginForm})
