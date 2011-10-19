# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Period'
        db.create_table('imc_period', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('finish', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('imc', ['Period'])

        # Adding unique constraint on 'Period', fields ['start', 'finish']
        db.create_unique('imc_period', ['start', 'finish'])

        # Adding model 'Showing'
        db.create_table('imc_showing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imc.Movie'], unique=True)),
            ('period', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imc.Period'], unique=True)),
            ('watched', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('imc', ['Showing'])

        # Adding unique constraint on 'Showing', fields ['movie', 'period']
        db.create_unique('imc_showing', ['movie_id', 'period_id'])

        # Deleting field 'Movie.finish'
        db.delete_column('imc_movie', 'finish')

        # Deleting field 'Movie.start'
        db.delete_column('imc_movie', 'start')


    def backwards(self, orm):
        
        # Removing unique constraint on 'Showing', fields ['movie', 'period']
        db.delete_unique('imc_showing', ['movie_id', 'period_id'])

        # Removing unique constraint on 'Period', fields ['start', 'finish']
        db.delete_unique('imc_period', ['start', 'finish'])

        # Deleting model 'Period'
        db.delete_table('imc_period')

        # Deleting model 'Showing'
        db.delete_table('imc_showing')

        # Adding field 'Movie.finish'
        db.add_column('imc_movie', 'finish', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Movie.start'
        db.add_column('imc_movie', 'start', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'imc.movie': {
            'Meta': {'object_name': 'Movie'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']"}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'imdb_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'imdb_rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plot': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'writer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'imc.period': {
            'Meta': {'unique_together': "(('start', 'finish'),)", 'object_name': 'Period'},
            'finish': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'imc.rating': {
            'Meta': {'unique_together': "(('user', 'movie'),)", 'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['imc.Movie']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']"})
        },
        'imc.showing': {
            'Meta': {'unique_together': "(('movie', 'period'),)", 'object_name': 'Showing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['imc.Movie']", 'unique': 'True'}),
            'period': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['imc.Period']", 'unique': 'True'}),
            'watched': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile', '_ormbases': ['auth.User']},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'posh_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ssh_key': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['imc']