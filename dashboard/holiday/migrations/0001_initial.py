# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HolidayRequest'
        db.create_table('holiday_holidayrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Profile'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_made', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('administrator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='admin_set', null=True, to=orm['profiles.Profile'])),
            ('employee_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('manager_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('holiday', ['HolidayRequest'])

        # Adding model 'Holiday'
        db.create_table('holiday_holiday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('holiday_request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['holiday.HolidayRequest'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('half_day', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('holiday', ['Holiday'])

        # Adding model 'BankHoliday'
        db.create_table('holiday_bankholiday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(default='bank holiday', max_length=255)),
        ))
        db.send_create_signal('holiday', ['BankHoliday'])


    def backwards(self, orm):
        
        # Deleting model 'HolidayRequest'
        db.delete_table('holiday_holidayrequest')

        # Deleting model 'Holiday'
        db.delete_table('holiday_holiday')

        # Deleting model 'BankHoliday'
        db.delete_table('holiday_bankholiday')


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
        'holiday.bankholiday': {
            'Meta': {'ordering': "['-date']", 'object_name': 'BankHoliday'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'bank holiday'", 'max_length': '255'})
        },
        'holiday.holiday': {
            'Meta': {'ordering': "['date']", 'object_name': 'Holiday'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'half_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'holiday_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['holiday.HolidayRequest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'holiday.holidayrequest': {
            'Meta': {'object_name': 'HolidayRequest'},
            'administrator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'admin_set'", 'null': 'True', 'to': "orm['profiles.Profile']"}),
            'date_made': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']"}),
            'employee_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile', '_ormbases': ['auth.User']},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'holiday_per_annum': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'managed_employees'", 'null': 'True', 'to': "orm['profiles.Profile']"}),
            'posh_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ssh_key': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['holiday']
