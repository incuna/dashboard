# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Item'
        db.create_table(u'items', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('bought', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('shoppinglist', ['Item'])


    def backwards(self, orm):
        
        # Deleting model 'Item'
        db.delete_table(u'items')


    models = {
        'shoppinglist.item': {
            'Meta': {'object_name': 'Item', 'db_table': "u'items'"},
            'bought': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['shoppinglist']
