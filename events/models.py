from django.db import models

from sponsor.models import *
from organizer.models import *

# Create your models here.
class Event(models.Model):
	#M2O Events => Organizer
	organizer = models.ForeignKey(Organizer) 
	create_date = models.DateTimeField(auto_now_add=True)
	event_date = models.DateTimeField()
	name = models.CharField(max_length=charFieldMaxLength)
	description = models.CharField(max_length=charFieldMaxLength)
	# seeking_type = # O2M with Seeking_type_Event

class Event_Sponsorship(models.Model):
	sponsor = models.ForeignKey(Sponsor)
	event = models.ForeignKey(Event)
	date = models.DateTimeField(auto_now_add=True)
	# sponsorship_type = #O2M with Sponsorship_type_Sponsor_Event

class Event_Sponsorship_Preferences(models.Model):
	event = models.ForeignKey(Event)
	# Data codes: 1 = funds, 2 = space, 3 = people, 4 = food
	FUNDS = 1
	SPACE = 2
	PEOPLE = 3
	FOOD = 4
	sponsorship_type_choices = (
		(FUNDS, "Funds"),
		(SPACE, "Space"),
		(PEOPLE, "People"),
		(FOOD, "Food"),
	)
	sponsorship_type = models.IntegerField(choices=sponsorship_type_choices)
	sponsorship_amount = models.CharField(max_length=charFieldMaxLength)

class Event_Sponsorship_Type(models.Model):
	event_sponsorship = models.ForeignKey(Event_Sponsorship)
	# Data codes: 1 = funds, 2 = space, 3 = people, 4 = food
	FUNDS = 1
	SPACE = 2
	PEOPLE = 3
	FOOD = 4
	sponsorship_type_choices = (
		(FUNDS, "Funds"),
		(SPACE, "Space"),
		(PEOPLE, "People"),
		(FOOD, "Food"),
	)
	sponsorship_type = models.IntegerField(choices=sponsorship_type_choices)
