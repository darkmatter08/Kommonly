from django.db import models
from django.contrib.auth.models import User

from sponsor.models import *
from sponsor.models import charFieldMaxLength

# Represents an Organizer, a user that creates and manages events
# He seeks sponsorships for his event
class Organizer(models.Model):
	user = models.ForeignKey(User)	
	organization = models.CharField(max_length=charFieldMaxLength)