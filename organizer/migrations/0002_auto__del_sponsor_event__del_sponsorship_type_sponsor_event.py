# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Sponsor_Event'
        db.delete_table(u'organizer_sponsor_event')

        # Deleting model 'Sponsorship_type_Sponsor_Event'
        db.delete_table(u'organizer_sponsorship_type_sponsor_event')


    def backwards(self, orm):
        # Adding model 'Sponsor_Event'
        db.create_table(u'organizer_sponsor_event', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizer.Organizer'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'organizer', ['Sponsor_Event'])

        # Adding model 'Sponsorship_type_Sponsor_Event'
        db.create_table(u'organizer_sponsorship_type_sponsor_event', (
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sponsor_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizer.Sponsor_Event'])),
        ))
        db.send_create_signal(u'organizer', ['Sponsorship_type_Sponsor_Event'])


    models = {
        u'organizer.event': {
            'Meta': {'object_name': 'Event'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizer.Organizer']"})
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
        u'organizer.seeking_type_event': {
            'Meta': {'object_name': 'Seeking_type_Event'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizer.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsorship_amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sponsorship_type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['organizer']