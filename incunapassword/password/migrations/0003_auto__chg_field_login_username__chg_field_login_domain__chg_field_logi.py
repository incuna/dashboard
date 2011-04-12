# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Login.username'
        db.alter_column('password_login', 'username', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Login.domain'
        db.alter_column('password_login', 'domain', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Login.name'
        db.alter_column('password_login', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Password.password'
        db.alter_column('password_password', 'password', self.gf('django.db.models.fields.CharField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Login.username'
        db.alter_column('password_login', 'username', self.gf('django.db.models.fields.TextField')(max_length=255))

        # Changing field 'Login.domain'
        db.alter_column('password_login', 'domain', self.gf('django.db.models.fields.TextField')(max_length=255))

        # Changing field 'Login.name'
        db.alter_column('password_login', 'name', self.gf('django.db.models.fields.TextField')(max_length=255))

        # Changing field 'Password.password'
        db.alter_column('password_password', 'password', self.gf('django.db.models.fields.TextField')(max_length=255))


    models = {
        'password.login': {
            'Meta': {'object_name': 'Login'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'password.password': {
            'Meta': {'object_name': 'Password'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['password.Login']"})
        }
    }

    complete_apps = ['password']
