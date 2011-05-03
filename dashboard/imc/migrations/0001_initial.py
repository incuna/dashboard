# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FilmBuff'
        db.create_table('imc_filmbuff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('is_film_buff', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('imc', ['FilmBuff'])

        # Adding model 'Month'
        db.create_table('imc_month', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal('imc', ['Month'])

        # Adding model 'Movie'
        db.create_table(u'movies', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('view_by', self.gf('django.db.models.fields.DateField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('imdb_id', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('imdb_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('thumbnail', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('plot', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('writer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('imdb_rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal('imc', ['Movie'])

        # Adding model 'UserRating'
        db.create_table(u'user_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imc.FilmBuff'])),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imc.Movie'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2, blank=True)),
        ))
        db.send_create_signal('imc', ['UserRating'])


    def backwards(self, orm):
        
        # Deleting model 'FilmBuff'
        db.delete_table('imc_filmbuff')

        # Deleting model 'Month'
        db.delete_table('imc_month')

        # Deleting model 'Movie'
        db.delete_table(u'movies')

        # Deleting model 'UserRating'
        db.delete_table(u'user_rating')


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
        'imc.filmbuff': {
            'Meta': {'object_name': 'FilmBuff'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_film_buff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'imc.month': {
            'Meta': {'object_name': 'Month'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'imc.movie': {
            'Meta': {'object_name': 'Movie', 'db_table': "u'movies'"},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'imdb_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'imdb_rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plot': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'view_by': ('django.db.models.fields.DateField', [], {}),
            'writer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'imc.userrating': {
            'Meta': {'object_name': 'UserRating', 'db_table': "u'user_rating'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['imc.Movie']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['imc.FilmBuff']"})
        }
    }

    complete_apps = ['imc']
