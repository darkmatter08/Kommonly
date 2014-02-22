from django.db import models

# Create your models here.
from sponsor.models import *
from django.contrib.auth.models import User


sponsorship_type_choices = (
	(1, "Funds"),
	(2, "Space"),
	(3, "People"),
	(4, "Food"),
)
charFieldMaxLength = 50

class Organizer(models.Model):
	user = models.ForeignKey(User)	
	organization = models.CharField(max_length=charFieldMaxLength)
	# event = # O2M with event
