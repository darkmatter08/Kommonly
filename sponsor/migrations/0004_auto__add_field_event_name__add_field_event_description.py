# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.name'
        db.add_column(u'sponsor_event', 'name',
                      self.gf('django.db.models.fields.CharField')(default='startup', max_length=50),
                      keep_default=False)

        # Adding field 'Event.description'
        db.add_column(u'sponsor_event', 'description',
                      self.gf('django.db.models.fields.CharField')(default='today', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.name'
        db.delete_column(u'sponsor_event', 'name')

        # Deleting field 'Event.description'
        db.delete_column(u'sponsor_event', 'description')


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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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