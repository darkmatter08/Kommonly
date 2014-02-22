# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizer.Organizer'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'Sponsor_Event'
        db.create_table(u'events_sponsor_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Sponsor_Event'])

        # Adding model 'Seeking_type_Event'
        db.create_table(u'events_seeking_type_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
            ('sponsorship_amount', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['Seeking_type_Event'])

        # Adding model 'Sponsorship_type_Sponsor_Event'
        db.create_table(u'events_sponsorship_type_sponsor_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsor_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Sponsor_Event'])),
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'events', ['Sponsorship_type_Sponsor_Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'Sponsor_Event'
        db.delete_table(u'events_sponsor_event')

        # Deleting model 'Seeking_type_Event'
        db.delete_table(u'events_seeking_type_event')

        # Deleting model 'Sponsorship_type_Sponsor_Event'
        db.delete_table(u'events_sponsorship_type_sponsor_event')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizer.Organizer']"})
        },
        u'events.seeking_type_event': {
            'Meta': {'object_name': 'Seeking_type_Event'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsorship_amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sponsorship_type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'events.sponsor_event': {
            'Meta': {'object_name': 'Sponsor_Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor']"})
        },
        u'events.sponsorship_type_sponsor_event': {
            'Meta': {'object_name': 'Sponsorship_type_Sponsor_Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor_event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Sponsor_Event']"}),
            'sponsorship_type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'organizer.organizer': {
            'Meta': {'object_name': 'Organizer'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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

    complete_apps = ['events']