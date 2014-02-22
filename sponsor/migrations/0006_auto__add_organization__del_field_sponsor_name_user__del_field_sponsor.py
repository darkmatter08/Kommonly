# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'sponsor_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('employees', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('locations', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_logo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'sponsor', ['Organization'])

        # Deleting field 'Sponsor.name_user'
        db.delete_column(u'sponsor_sponsor', 'name_user')

        # Deleting field 'Sponsor.join_date'
        db.delete_column(u'sponsor_sponsor', 'join_date')

        # Deleting field 'Sponsor.password'
        db.delete_column(u'sponsor_sponsor', 'password')

        # Deleting field 'Sponsor.email'
        db.delete_column(u'sponsor_sponsor', 'email')

        # Adding field 'Sponsor.user'
        db.add_column(u'sponsor_sponsor', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


        # Renaming column for 'Sponsor.organization' to match new field type.
        db.rename_column(u'sponsor_sponsor', 'organization', 'organization_id')
        # Changing field 'Sponsor.organization'
        db.alter_column(u'sponsor_sponsor', 'organization_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sponsor.Organization']))
        # Adding index on 'Sponsor', fields ['organization']
        db.create_index(u'sponsor_sponsor', ['organization_id'])


    def backwards(self, orm):
        # Removing index on 'Sponsor', fields ['organization']
        db.delete_index(u'sponsor_sponsor', ['organization_id'])

        # Deleting model 'Organization'
        db.delete_table(u'sponsor_organization')

        # Adding field 'Sponsor.name_user'
        db.add_column(u'sponsor_sponsor', 'name_user',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Sponsor.join_date'
        db.add_column(u'sponsor_sponsor', 'join_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=1, blank=True),
                      keep_default=False)

        # Adding field 'Sponsor.password'
        db.add_column(u'sponsor_sponsor', 'password',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Sponsor.email'
        db.add_column(u'sponsor_sponsor', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75, unique=True),
                      keep_default=False)

        # Deleting field 'Sponsor.user'
        db.delete_column(u'sponsor_sponsor', 'user_id')


        # Renaming column for 'Sponsor.organization' to match new field type.
        db.rename_column(u'sponsor_sponsor', 'organization_id', 'organization')
        # Changing field 'Sponsor.organization'
        db.alter_column(u'sponsor_sponsor', 'organization', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'employees': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_logo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'locations': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sponsor.Organization']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['sponsor']