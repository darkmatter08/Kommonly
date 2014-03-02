# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sponsor_types_organization'
        db.create_table(u'sponsor_sponsor_types_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Organization'])),
            ('funding_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Sponsor_types'])),
        ))
        db.send_create_signal(u'sponsor', ['Sponsor_types_organization'])

        # Adding model 'Sponsor_types'
        db.create_table(u'sponsor_sponsor_types', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('funding_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sponsor', ['Sponsor_types'])

        # Deleting field 'Organization.site'
        db.delete_column(u'sponsor_organization', 'site')

        # Deleting field 'Organization.locations'
        db.delete_column(u'sponsor_organization', 'locations')

        # Adding field 'Organization.location'
        db.add_column(u'sponsor_organization', 'location',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Organization.email'
        db.add_column(u'sponsor_organization', 'email',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Organization.phone'
        db.add_column(u'sponsor_organization', 'phone',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Organization.website'
        db.add_column(u'sponsor_organization', 'website',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)


        # Changing field 'Organization.image_logo'
        db.alter_column(u'sponsor_organization', 'image_logo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Organization.employees'
        db.alter_column(u'sponsor_organization', 'employees', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Organization.name'
        db.alter_column(u'sponsor_organization', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting model 'Sponsor_types_organization'
        db.delete_table(u'sponsor_sponsor_types_organization')

        # Deleting model 'Sponsor_types'
        db.delete_table(u'sponsor_sponsor_types')

        # Adding field 'Organization.site'
        db.add_column(u'sponsor_organization', 'site',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Organization.locations'
        db.add_column(u'sponsor_organization', 'locations',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Deleting field 'Organization.location'
        db.delete_column(u'sponsor_organization', 'location')

        # Deleting field 'Organization.email'
        db.delete_column(u'sponsor_organization', 'email')

        # Deleting field 'Organization.phone'
        db.delete_column(u'sponsor_organization', 'phone')

        # Deleting field 'Organization.website'
        db.delete_column(u'sponsor_organization', 'website')


        # Changing field 'Organization.image_logo'
        db.alter_column(u'sponsor_organization', 'image_logo', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Organization.employees'
        db.alter_column(u'sponsor_organization', 'employees', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Organization.name'
        db.alter_column(u'sponsor_organization', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

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
        u'sponsor.organization': {
            'Meta': {'object_name': 'Organization'},
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
        },
        u'sponsor.sponsor_types_organization': {
            'Meta': {'object_name': 'Sponsor_types_organization'},
            'funding_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Sponsor_types']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Organization']"})
        }
    }

    complete_apps = ['sponsor']