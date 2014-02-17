from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from sponsor.models import *


sponsorship_type_choices = (
	(1, "Funds"),
	(2, "Space"),
	(3, "People"),
	(4, "Food"),
)
charFieldMaxLength = 50

class Organizer(models.Model):
	user = models.OneToOneField(User)
	organization = models.CharField(max_length=charFieldMaxLength)
	# event = # O2M with event

