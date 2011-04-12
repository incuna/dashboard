# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Password'
        db.create_table('password_password', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['password.Username'])),
        ))
        db.send_create_signal('password', ['Password'])

        # Adding model 'Username'
        db.create_table('password_username', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('domain', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal('password', ['Username'])


    def backwards(self, orm):
        
        # Deleting model 'Password'
        db.delete_table('password_password')

        # Deleting model 'Username'
        db.delete_table('password_username')


    models = {
        'password.password': {
            'Meta': {'object_name': 'Password'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['password.Username']"})
        },
        'password.username': {
            'Meta': {'object_name': 'Username'},
            'domain': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['password']
