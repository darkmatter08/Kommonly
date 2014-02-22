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

