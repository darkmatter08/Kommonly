from django.db import models

from organizer.models import *
# Create your models here.

charFieldMaxLength = 50

class Sponsor(models.Model):
	name_user = models.CharField(max_length=charFieldMaxLength)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=charFieldMaxLength)
	organization = models.CharField(max_length=charFieldMaxLength)
	join_date = models.DateTimeField(auto_now_add=True)
	# M2M Sponsors and events, through Sponsor_Event
	backed_event = models.ManyToManyField('Event', through='Sponsor_Event')

class Event(models.Model):
	#M2O Events => Organizer
	organizer = models.ForeignKey(Organizer) 
	create_date = models.DateTimeField(auto_now_add=True)
	event_date = models.DateTimeField()
	# seeking_type = # O2M with Seeking_type_Event

class Sponsor_Event(models.Model):
	sponsor = models.ForeignKey(Sponsor)
	event = models.ForeignKey(Event)
	date = models.DateTimeField(auto_now_add=True)
	# sponsorship_type = #O2M with Sponsorship_type_Sponsor_Event

class Seeking_type_Event(models.Model):
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

class Sponsorship_type_Sponsor_Event(models.Model):
	sponsor_event = models.ForeignKey(Sponsor_Event)
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
