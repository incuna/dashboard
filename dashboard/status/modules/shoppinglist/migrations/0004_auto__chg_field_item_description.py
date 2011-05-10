# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Item.description'
        db.alter_column(u'items', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    def backwards(self, orm):
        
        # Changing field 'Item.description'
        db.alter_column(u'items', 'description', self.gf('django.db.models.fields.TextField')(null=True))


    models = {
        'shoppinglist.item': {
            'Meta': {'object_name': 'Item', 'db_table': "u'items'"},
            'bought': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['shoppinglist']
