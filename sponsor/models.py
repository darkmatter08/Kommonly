from django.db import models

# Create your models here.

charFieldMaxLength = 50


class Sponsor(models.Model):
	name_user = models.CharField(max_length=charFieldMaxLength)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=charFieldMaxLength)
	organization = models.CharField(max_length=charFieldMaxLength)
	join_date = models.DateTimeField(auto_now_add=True)
	# M2M Sponsors and events, through Sponsor_Event
	# backed_event = models.ManyToManyField('Event', through='Sponsor_Event')
