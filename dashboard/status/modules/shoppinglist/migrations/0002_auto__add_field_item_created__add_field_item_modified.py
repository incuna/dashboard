# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Item.created'
        db.add_column(u'items', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 1, 10, 12, 48, 38, 839744), blank=True), keep_default=False)

        # Adding field 'Item.modified'
        db.add_column(u'items', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 1, 10, 12, 48, 45, 543666), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Item.created'
        db.delete_column(u'items', 'created')

        # Deleting field 'Item.modified'
        db.delete_column(u'items', 'modified')


    models = {
        'shoppinglist.item': {
            'Meta': {'object_name': 'Item', 'db_table': "u'items'"},
            'bought': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['shoppinglist']
