from django.db import models

from organizer.models import *
# Create your models here.
from django.utils import timezone

charFieldMaxLength = 100

class Organization(models.Model):
	name = models.CharField(max_length=charFieldMaxLength)
	employees = models.CharField(max_length=charFieldMaxLength)
	location = models.CharField(max_length=charFieldMaxLength)
	email = models.CharField(max_length=charFieldMaxLength)
	phone = models.CharField(max_length=charFieldMaxLength)
	
	contact_fname = models.CharField(max_length=charFieldMaxLength)
	contact_lname = models.CharField(max_length=charFieldMaxLength)
	# Link to their logo
	image_logo = models.CharField(max_length=charFieldMaxLength) 
	description = models.CharField(max_length=3000)
	website = models.CharField(max_length=charFieldMaxLength)
	created_at  = models.DateField(default=timezone.now)
	
class Sponsor(models.Model):
	user = models.ForeignKey(User)
	organization = models.ForeignKey(Organization)

class Sponsor_types(models.Model):
	funding_type = models.CharField(max_length=charFieldMaxLength)

class Sponsor_types_organization(models.Model):
	organization = models.ForeignKey(Organization)	
	funding_type = models.ForeignKey(Sponsor_types)

