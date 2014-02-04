# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Seeking_type_Event'
        db.create_table(u'sponsor_seeking_type_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Event'])),
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
            ('sponsorship_amount', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'sponsor', ['Seeking_type_Event'])

        # Adding model 'Event'
        db.create_table(u'sponsor_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizer.Organizer'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'sponsor', ['Event'])


        # Changing field 'Sponsor_Event.event'
        db.alter_column(u'sponsor_sponsor_event', 'event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Event']))

    def backwards(self, orm):
        # Deleting model 'Seeking_type_Event'
        db.delete_table(u'sponsor_seeking_type_event')

        # Deleting model 'Event'
        db.delete_table(u'sponsor_event')


        # Changing field 'Sponsor_Event.event'
        db.alter_column(u'sponsor_sponsor_event', 'event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizer.Organizer']))

    models = {
        u'organizer.organizer': {
            'Meta': {'object_name': 'Organizer'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sponsor.event': {
            'Meta': {'object_name': 'Event'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizer.Organizer']"})
        },
        u'sponsor.seeking_type_event': {
            'Meta': {'object_name': 'Seeking_type_Event'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsorship_amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sponsorship_type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'backed_event': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sponsor.Event']", 'through': u"orm['sponsor.Sponsor_Event']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name_user': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sponsor.sponsor_event': {
            'Meta': {'object_name': 'Sponsor_Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor']"})
        },
        u'sponsor.sponsorship_type_sponsor_event': {
            'Meta': {'object_name': 'Sponsorship_type_Sponsor_Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor_event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor_Event']"}),
            'sponsorship_type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['sponsor']