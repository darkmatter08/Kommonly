# Shawn Jain 
# 2/22/2014
# Kommonly project

# imports
from django.db import models
from django import forms
from events.models import *
from sponsor.models import *
from django.forms import ModelForm, Textarea

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class EventForm(forms.ModelForm):
	# for item in Sponsor_types.objects.all():
	# 	exec(item.funding_type + " = forms.BooleanField(required=False)")
	
	sponsorshipTypeLookup = {"id_new_1": 1, "id_new_2": 2, "id_new_3": 3, "id_new_4": 4}
	## OLD PREFERENCES:::
	# def __init__(self, *args, **kwargs):
	# 	options = kwargs.pop('options')
	# 	selected = kwargs.pop('selected', [])
	# 	print "selected in eventForm: " + str(selected)
	# 	print "options in eventForm: " + str(options)
	# 	for option in options:
	# 		print str(option.id)
	# 	print "----"
	# 	print "length of options: " + str(len(options))
	# 	super(EventForm, self).__init__(*args, **kwargs)
	# 	for index in range(len(options)):
	# 		if options[index].id in selected:
	# 			print "in selected: " + str(options[index].id)
	# 			self.fields['{option}'.format(option=options[index].id)] = forms.BooleanField(required=False, label=options[index].funding_type, initial=True)
	# 		else:
	# 			self.fields['{option}'.format(option=options[index].id)] = forms.BooleanField(required=False, label=options[index].funding_type)
	def __init__(self, *args, **kwargs):
		expected_reach1 = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Event
		fields = ['name', 'event_date', 'expected_reach', 'description']
		widgets = {
            'expected_reach': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

# class Event_Sponsorship_PreferencesForm(forms.ModelForm):
# 	class Meta:
# 		model = Event_Sponsorship_Preferences
# 		fields = ['sponsorship_type', 'sponsorship_amount']
# 		widgets = {
# 			'sponsorship_type': forms.CheckboxSelectMultiple()
# 		}

# class Event_Sponsorship_PreferencesForm(forms.Form):
# 	# sponsorship_type_choices_inv = dict(Sponsor_types.objects.all())
# 	for item in Sponsor_types.objects.all():
# 		exec(item.funding_type + " = forms.BooleanField(required=False)")
		# exec(item.funding_type + "_desc = forms.CharField(required=False)")
	# sponsorship_type_choices = {v:k for k, v in sponsorship_type_choices_inv.items()}
	# sponsorship_type_choices["Funds"]
	# funds = forms.BooleanField(required=False)

