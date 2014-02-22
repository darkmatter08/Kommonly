# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Sponsorship_type_Sponsor_Event'
        db.delete_table(u'sponsor_sponsorship_type_sponsor_event')

        # Deleting model 'Seeking_type_Event'
        db.delete_table(u'sponsor_seeking_type_event')

        # Deleting model 'Sponsor_Event'
        db.delete_table(u'sponsor_sponsor_event')

        # Deleting model 'Event'
        db.delete_table(u'sponsor_event')


    def backwards(self, orm):
        # Adding model 'Sponsorship_type_Sponsor_Event'
        db.create_table(u'sponsor_sponsorship_type_sponsor_event', (
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsor_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor_Event'])),
        ))
        db.send_create_signal(u'sponsor', ['Sponsorship_type_Sponsor_Event'])

        # Adding model 'Seeking_type_Event'
        db.create_table(u'sponsor_seeking_type_event', (
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Event'])),
            ('sponsorship_amount', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'sponsor', ['Seeking_type_Event'])

        # Adding model 'Sponsor_Event'
        db.create_table(u'sponsor_sponsor_event', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Event'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'sponsor', ['Sponsor_Event'])

        # Adding model 'Event'
        db.create_table(u'sponsor_event', (
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('organizer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizer.Organizer'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'sponsor', ['Event'])


    models = {
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sponsor']