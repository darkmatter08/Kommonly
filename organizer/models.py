from django.db import models

# Create your models here.
from sponsor.models import *

class Organizer(models.Model):
	name_user = models.CharField(max_length=charFieldMaxLength)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=charFieldMaxLength)
	organization = models.CharField(max_length=charFieldMaxLength)
	join_date = models.DateTimeField(auto_now_add=True)
	# event = # O2M with event


class Event(models.Model):
	#M2O Events => Organizer
	organizer = models.ForeignKey(Organizer) 
	create_date = models.DateTimeField(auto_now_add=True)
	event_date = models.DateTimeField()
	# seeking_type = # O2M with Seeking_type_Event

class Sponsor_Event(models.Model):
	sponsor = models.ForeignKey(Sponsor)
	event = models.ForeignKey(Organizer)
	date = models.DateTimeField(auto_now_add=True)
	# sponsorship_type = #O2M with Sponsorship_type_Sponsor_Event

class Sponsorship_type_Sponsor_Event(models.Model):
	sponsor_event = models.ForeignKey(Sponsor_Event)
	# Data codes: 1 = funds, 2 = space, 3 = people, 4 = food
	sponsorship_type = models.IntegerField()

class Seeking_type_Event(models.Model):
	event = models.ForeignKey(Event)
	# Data codes: 1 = funds, 2 = space, 3 = people, 4 = food
	sponsorship_type = models.IntegerField()
	sponsorship_amount = models.CharField(max_length=charFieldMaxLength)
