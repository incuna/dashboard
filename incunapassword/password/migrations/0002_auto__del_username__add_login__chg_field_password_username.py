# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Username'
        db.delete_table('password_username')

        # Adding model 'Login'
        db.create_table('password_login', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('domain', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal('password', ['Login'])

        # Changing field 'Password.username'
        db.alter_column('password_password', 'username_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['password.Login']))


    def backwards(self, orm):
        
        # Adding model 'Username'
        db.create_table('password_username', (
            ('username', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('domain', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal('password', ['Username'])

        # Deleting model 'Login'
        db.delete_table('password_login')

        # Changing field 'Password.username'
        db.alter_column('password_password', 'username_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['password.Username']))


    models = {
        'password.login': {
            'Meta': {'object_name': 'Login'},
            'domain': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        'password.password': {
            'Meta': {'object_name': 'Password'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['password.Login']"})
        }
    }

    complete_apps = ['password']
