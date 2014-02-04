from django.db import models

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
	name_user = models.CharField(max_length=charFieldMaxLength)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=charFieldMaxLength)
	organization = models.CharField(max_length=charFieldMaxLength)
	join_date = models.DateTimeField(auto_now_add=True)
	# event = # O2M with event
