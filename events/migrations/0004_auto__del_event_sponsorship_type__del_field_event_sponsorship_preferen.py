# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Event_Sponsorship_Type'
        db.delete_table(u'events_event_sponsorship_type')

        # Deleting field 'Event_Sponsorship_Preferences.sponsorship_amount'
        db.delete_column(u'events_event_sponsorship_preferences', 'sponsorship_amount')


        # Renaming column for 'Event_Sponsorship_Preferences.sponsorship_type' to match new field type.
        db.rename_column(u'events_event_sponsorship_preferences', 'sponsorship_type', 'sponsorship_type_id')
        # Changing field 'Event_Sponsorship_Preferences.sponsorship_type'
        db.alter_column(u'events_event_sponsorship_preferences', 'sponsorship_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor_types']))
        # Adding index on 'Event_Sponsorship_Preferences', fields ['sponsorship_type']
        db.create_index(u'events_event_sponsorship_preferences', ['sponsorship_type_id'])


    def backwards(self, orm):
        # Removing index on 'Event_Sponsorship_Preferences', fields ['sponsorship_type']
        db.delete_index(u'events_event_sponsorship_preferences', ['sponsorship_type_id'])

        # Adding model 'Event_Sponsorship_Type'
        db.create_table(u'events_event_sponsorship_type', (
            ('event_sponsorship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event_Sponsorship'])),
            ('sponsorship_type', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'events', ['Event_Sponsorship_Type'])

        # Adding field 'Event_Sponsorship_Preferences.sponsorship_amount'
        db.add_column(u'events_event_sponsorship_preferences', 'sponsorship_amount',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)


        # Renaming column for 'Event_Sponsorship_Preferences.sponsorship_type' to match new field type.
        db.rename_column(u'events_event_sponsorship_preferences', 'sponsorship_type_id', 'sponsorship_type')
        # Changing field 'Event_Sponsorship_Preferences.sponsorship_type'
        db.alter_column(u'events_event_sponsorship_preferences', 'sponsorship_type', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'expected_reach': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizer.Organizer']"})
        },
        u'events.event_image': {
            'Meta': {'object_name': 'Event_Image'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'default': "'assets/None/no-img.jpg'", 'max_length': '100'})
        },
        u'events.event_sponsorship': {
            'Meta': {'object_name': 'Event_Sponsorship'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor']"})
        },
        u'events.event_sponsorship_preferences': {
            'Meta': {'object_name': 'Event_Sponsorship_Preferences'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsorship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor_types']"})
        },
        u'organizer.organizer': {
            'Meta': {'object_name': 'Organizer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'sponsor.organization': {
            'Meta': {'object_name': 'Organization'},
            'contact_fname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_lname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'employees': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_logo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Organization']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'sponsor.sponsor_types': {
            'Meta': {'object_name': 'Sponsor_types'},
            'funding_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['events']