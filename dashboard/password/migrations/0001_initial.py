# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Login'
        db.create_table('password_login', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('passwd', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('password', ['Login'])


    def backwards(self, orm):
        
        # Deleting model 'Login'
        db.delete_table('password_login')


    models = {
        'password.login': {
            'Meta': {'object_name': 'Login'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'passwd': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['password']
