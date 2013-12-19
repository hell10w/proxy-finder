# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Proxy.country_code'
        db.add_column(u'proxyfinder_proxy', 'country_code',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=5, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Proxy.country_code'
        db.delete_column(u'proxyfinder_proxy', 'country_code')


    models = {
        u'proxyfinder.proxy': {
            'Meta': {'unique_together': "[['ip', 'port']]", 'object_name': 'Proxy'},
            'checked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'port': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'proxyfinder.site': {
            'Meta': {'object_name': 'Site'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'proxyfinder.url': {
            'Meta': {'object_name': 'Url'},
            'checked': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '10240'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proxyfinder.Site']"})
        }
    }

    complete_apps = ['proxyfinder']