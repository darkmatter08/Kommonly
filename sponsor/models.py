from django.db import models
from django.utils import timezone

from organizer.models import *

charFieldMaxLength = 100

# Represents a company or non-profit. It is associated with any number of
# sponsors that function to represent the organization. 
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

# Represents a Sponsor, a user associated with and representing an 
# Organization that offers sponsorships to Events created by Organizers 
class Sponsor(models.Model):
	user = models.ForeignKey(User)
	organization = models.ForeignKey(Organization)

# Represents a type of sponsorship. The original four types of sponsorships were
# 1) FUNDS 2) SPACE 3) PEOPLE 4) FOOD. This table is relatively static, functioning 
# as a 'datatype' for each type of sponsorship.
class Sponsor_types(models.Model):
	funding_type = models.CharField(max_length=charFieldMaxLength)

# Represents the type of sponsorships that an organization prefers to offer
# Transaction table for the Many to Many relationship between Organization and Sponsor_types
class Sponsor_types_organization(models.Model):
	organization = models.ForeignKey(Organization)	
	funding_type = models.ForeignKey(Sponsor_types)