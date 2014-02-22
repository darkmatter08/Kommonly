from django.db import models

from organizer.models import *
# Create your models here.

charFieldMaxLength = 50

class Organization(models.Model):
	name = models.CharField(max_length=charFieldMaxLength)
	employees = models.CharField(max_length=charFieldMaxLength)
	locations = models.CharField(max_length=charFieldMaxLength)
	# Link to their logo
	image_logo = models.CharField(max_length=charFieldMaxLength) 
	description = models.CharField(max_length=charFieldMaxLength)

class Sponsor(models.Model):
	user = models.ForeignKey(User)
	organization = models.ForeignKey(Organization)