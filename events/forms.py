# Shawn Jain 
# 2/22/2014
# Kommonly project

# imports
from django.db import models
from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()