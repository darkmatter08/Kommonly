from django.db import models

from sponsor.models import *
from organizer.models import *

# Represents an Event, created by an Organizer. 
class Event(models.Model):
	# One to Many - Organizer to Event
	organizer = models.ForeignKey(Organizer) 
	create_date = models.DateTimeField(auto_now_add=True)
	event_date = models.DateTimeField()
	name = models.CharField(max_length=charFieldMaxLength)
	description = models.CharField(max_length=charFieldMaxLength)
	expected_reach = models.CharField(max_length=50000)
	location = models.CharField(max_length=charFieldMaxLength)
	funding_sought = models.DecimalField(max_digits=8, decimal_places=2)

# Represents an agreed upon sponsorship
# Transaction Table for Many to Many relationship between Event and Sponsor
class Event_Sponsorship(models.Model):
	sponsor = models.ForeignKey(Sponsor)
	event = models.ForeignKey(Event)
	date = models.DateTimeField(auto_now_add=True)

# Represents a type of sponsorship sought for an event
# Transaction Table for Many to Many relationship between Event and Sponsorship_type
class Event_Sponsorship_Preferences(models.Model):
	event = models.ForeignKey(Event)
	sponsorship_type = models.ForeignKey(Sponsor_types)

# Saves an image associated with an event
class Event_Image(models.Model):
	pic = models.ImageField(upload_to='Kommonly/static/assets/', default='assets/None/no-img.jpg')
	# One to Many - Event and Image
	event = models.ForeignKey(Event)