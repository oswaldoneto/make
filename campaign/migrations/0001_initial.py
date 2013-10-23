# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'campaign_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'campaign', ['Campaign'])

        # Adding model 'Challenge'
        db.create_table(u'campaign_challenge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'])),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('job_profile', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('skill_required', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('job_estimate', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('reward', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('availability', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'campaign', ['Challenge'])


    def backwards(self, orm):
        # Deleting model 'Campaign'
        db.delete_table(u'campaign_campaign')

        # Deleting model 'Challenge'
        db.delete_table(u'campaign_challenge')


    models = {
        u'campaign.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'campaign.challenge': {
            'Meta': {'object_name': 'Challenge'},
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'job_estimate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'job_profile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reward': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'skill_required': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['campaign']