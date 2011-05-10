# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Attachments'
        db.create_table(u'attachments', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('container_id', self.gf('django.db.models.fields.IntegerField')()),
            ('container_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('disk_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('filesize', self.gf('django.db.models.fields.IntegerField')()),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('digest', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('downloads', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['Attachments'])

        # Adding model 'Boards'
        db.create_table(u'boards', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('topics_count', self.gf('django.db.models.fields.IntegerField')()),
            ('messages_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_message_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Boards'])

        # Adding model 'AuthSources'
        db.create_table(u'auth_sources', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('port', self.gf('django.db.models.fields.IntegerField')()),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('account_password', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('base_dn', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('attr_login', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('attr_firstname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('attr_lastname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('attr_mail', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('onthefly_register', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tls', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('redmine', ['AuthSources'])

        # Adding model 'Changesets'
        db.create_table(u'changesets', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('repository_id', self.gf('django.db.models.fields.IntegerField')()),
            ('revision', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('committer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('committed_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('commit_date', self.gf('django.db.models.fields.DateField')()),
            ('scmid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Changesets'])

        # Adding model 'ChangesetsIssues'
        db.create_table(u'changesets_issues', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changeset_id', self.gf('django.db.models.fields.IntegerField')()),
            ('issue_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['ChangesetsIssues'])

        # Adding model 'Comments'
        db.create_table(u'comments', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('commented_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('commented_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['Comments'])

        # Adding model 'CustomFields'
        db.create_table(u'custom_fields', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('field_format', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('possible_values', self.gf('django.db.models.fields.TextField')()),
            ('regexp', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('min_length', self.gf('django.db.models.fields.IntegerField')()),
            ('max_length', self.gf('django.db.models.fields.IntegerField')()),
            ('is_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_for_all', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_filter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('searchable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('default_value', self.gf('django.db.models.fields.TextField')()),
            ('editable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('redmine', ['CustomFields'])

        # Adding model 'CustomFieldsProjects'
        db.create_table(u'custom_fields_projects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('custom_field_id', self.gf('django.db.models.fields.IntegerField')()),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['CustomFieldsProjects'])

        # Adding model 'CustomFieldsTrackers'
        db.create_table(u'custom_fields_trackers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('custom_field_id', self.gf('django.db.models.fields.IntegerField')()),
            ('tracker_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['CustomFieldsTrackers'])

        # Adding model 'EnabledModules'
        db.create_table(u'enabled_modules', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['EnabledModules'])

        # Adding model 'CustomValues'
        db.create_table(u'custom_values', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('customized_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('customized_id', self.gf('django.db.models.fields.IntegerField')()),
            ('custom_field_id', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('redmine', ['CustomValues'])

        # Adding model 'Documents'
        db.create_table(u'documents', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['Documents'])

        # Adding model 'Enumerations'
        db.create_table(u'enumerations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Enumerations'])

        # Adding model 'GroupsUsers'
        db.create_table(u'groups_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['GroupsUsers'])

        # Adding model 'IssueCategories'
        db.create_table(u'issue_categories', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('assigned_to_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['IssueCategories'])

        # Adding model 'IssueRelations'
        db.create_table(u'issue_relations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('issue_from_id', self.gf('django.db.models.fields.IntegerField')()),
            ('issue_to_id', self.gf('django.db.models.fields.IntegerField')()),
            ('relation_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('delay', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['IssueRelations'])

        # Adding model 'IssueStatus'
        db.create_table(u'issue_statuses', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('default_done_ratio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['IssueStatus'])

        # Adding model 'JournalDetails'
        db.create_table(u'journal_details', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('journal_id', self.gf('django.db.models.fields.IntegerField')()),
            ('property', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('prop_key', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('old_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['JournalDetails'])

        # Adding model 'Issue'
        db.create_table(u'issues', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('tracker_id', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redmine.Project'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redmine.IssueStatus'])),
            ('assigned_to_id', self.gf('django.db.models.fields.IntegerField')()),
            ('priority_id', self.gf('django.db.models.fields.IntegerField')()),
            ('fixed_version_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('lock_version', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('done_ratio', self.gf('django.db.models.fields.IntegerField')()),
            ('estimated_hours', self.gf('django.db.models.fields.FloatField')()),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')()),
            ('root_id', self.gf('django.db.models.fields.IntegerField')()),
            ('lft', self.gf('django.db.models.fields.IntegerField')()),
            ('rgt', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Issue'])

        # Adding model 'Journals'
        db.create_table(u'journals', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('journalized_id', self.gf('django.db.models.fields.IntegerField')()),
            ('journalized_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['Journals'])

        # Adding model 'MemberRoles'
        db.create_table(u'member_roles', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('member_id', self.gf('django.db.models.fields.IntegerField')()),
            ('role_id', self.gf('django.db.models.fields.IntegerField')()),
            ('inherited_from', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['MemberRoles'])

        # Adding model 'Member'
        db.create_table(u'members', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redmine.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redmine.Project'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('mail_notification', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('redmine', ['Member'])

        # Adding model 'Messages'
        db.create_table(u'messages', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('board_id', self.gf('django.db.models.fields.IntegerField')()),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('replies_count', self.gf('django.db.models.fields.IntegerField')()),
            ('last_reply_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('locked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sticky', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Messages'])

        # Adding model 'OpenIdAuthenticationNonces'
        db.create_table(u'open_id_authentication_nonces', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('server_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['OpenIdAuthenticationNonces'])

        # Adding model 'News'
        db.create_table(u'news', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('comments_count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['News'])

        # Adding model 'OpenIdAuthenticationAssociations'
        db.create_table(u'open_id_authentication_associations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('issued', self.gf('django.db.models.fields.IntegerField')()),
            ('lifetime', self.gf('django.db.models.fields.IntegerField')()),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('assoc_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('server_url', self.gf('django.db.models.fields.TextField')()),
            ('secret', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('redmine', ['OpenIdAuthenticationAssociations'])

        # Adding model 'Project'
        db.create_table(u'projects', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('homepage', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redmine.Project'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('lft', self.gf('django.db.models.fields.IntegerField')()),
            ('rgt', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Project'])

        # Adding model 'ProjectsTrackers'
        db.create_table(u'projects_trackers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('tracker_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['ProjectsTrackers'])

        # Adding model 'Queries'
        db.create_table(u'queries', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('filters', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('column_names', self.gf('django.db.models.fields.TextField')()),
            ('sort_criteria', self.gf('django.db.models.fields.TextField')()),
            ('group_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['Queries'])

        # Adding model 'Repositories'
        db.create_table(u'repositories', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('root_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['Repositories'])

        # Adding model 'Roles'
        db.create_table(u'roles', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('assignable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('builtin', self.gf('django.db.models.fields.IntegerField')()),
            ('permissions', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('redmine', ['Roles'])

        # Adding model 'SchemaMigrations'
        db.create_table(u'schema_migrations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('redmine', ['SchemaMigrations'])

        # Adding model 'Settings'
        db.create_table(u'settings', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.TextField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['Settings'])

        # Adding model 'TimeEntries'
        db.create_table(u'time_entries', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('issue_id', self.gf('django.db.models.fields.IntegerField')()),
            ('hours', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('activity_id', self.gf('django.db.models.fields.IntegerField')()),
            ('spent_on', self.gf('django.db.models.fields.DateField')()),
            ('tyear', self.gf('django.db.models.fields.IntegerField')()),
            ('tmonth', self.gf('django.db.models.fields.IntegerField')()),
            ('tweek', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['TimeEntries'])

        # Adding model 'Tokens'
        db.create_table(u'tokens', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['Tokens'])

        # Adding model 'Trackers'
        db.create_table(u'trackers', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_in_chlog', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('is_in_roadmap', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('redmine', ['Trackers'])

        # Adding model 'UserPreferences'
        db.create_table(u'user_preferences', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('others', self.gf('django.db.models.fields.TextField')()),
            ('hide_mail', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_zone', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['UserPreferences'])

        # Adding model 'User'
        db.create_table(u'users', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('hashed_password', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('mail_notification', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('last_login_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('auth_source_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('identity_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['User'])

        # Adding model 'Versions'
        db.create_table(u'versions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('effective_date', self.gf('django.db.models.fields.DateField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('wiki_page_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sharing', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['Versions'])

        # Adding model 'Watchers'
        db.create_table(u'watchers', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('watchable_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('watchable_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Watchers'])

        # Adding model 'WikiContentVersions'
        db.create_table(u'wiki_content_versions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('wiki_content_id', self.gf('django.db.models.fields.IntegerField')()),
            ('page_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('data', self.gf('django.db.models.fields.TextField')()),
            ('compression', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['WikiContentVersions'])

        # Adding model 'WikiContents'
        db.create_table(u'wiki_contents', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['WikiContents'])

        # Adding model 'WikiPages'
        db.create_table(u'wiki_pages', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('wiki_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('protected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['WikiPages'])

        # Adding model 'Workflows'
        db.create_table(u'workflows', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('tracker_id', self.gf('django.db.models.fields.IntegerField')()),
            ('old_status_id', self.gf('django.db.models.fields.IntegerField')()),
            ('new_status_id', self.gf('django.db.models.fields.IntegerField')()),
            ('role_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Workflows'])

        # Adding model 'WikiRedirects'
        db.create_table(u'wiki_redirects', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('wiki_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('redirects_to', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('redmine', ['WikiRedirects'])

        # Adding model 'Wikis'
        db.create_table(u'wikis', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('start_page', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redmine', ['Wikis'])

        # Adding model 'Changes'
        db.create_table(u'changes', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('changeset_id', self.gf('django.db.models.fields.IntegerField')()),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('path', self.gf('django.db.models.fields.TextField')()),
            ('from_path', self.gf('django.db.models.fields.TextField')()),
            ('from_revision', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('revision', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('redmine', ['Changes'])


    def backwards(self, orm):
        
        # Deleting model 'Attachments'
        db.delete_table(u'attachments')

        # Deleting model 'Boards'
        db.delete_table(u'boards')

        # Deleting model 'AuthSources'
        db.delete_table(u'auth_sources')

        # Deleting model 'Changesets'
        db.delete_table(u'changesets')

        # Deleting model 'ChangesetsIssues'
        db.delete_table(u'changesets_issues')

        # Deleting model 'Comments'
        db.delete_table(u'comments')

        # Deleting model 'CustomFields'
        db.delete_table(u'custom_fields')

        # Deleting model 'CustomFieldsProjects'
        db.delete_table(u'custom_fields_projects')

        # Deleting model 'CustomFieldsTrackers'
        db.delete_table(u'custom_fields_trackers')

        # Deleting model 'EnabledModules'
        db.delete_table(u'enabled_modules')

        # Deleting model 'CustomValues'
        db.delete_table(u'custom_values')

        # Deleting model 'Documents'
        db.delete_table(u'documents')

        # Deleting model 'Enumerations'
        db.delete_table(u'enumerations')

        # Deleting model 'GroupsUsers'
        db.delete_table(u'groups_users')

        # Deleting model 'IssueCategories'
        db.delete_table(u'issue_categories')

        # Deleting model 'IssueRelations'
        db.delete_table(u'issue_relations')

        # Deleting model 'IssueStatus'
        db.delete_table(u'issue_statuses')

        # Deleting model 'JournalDetails'
        db.delete_table(u'journal_details')

        # Deleting model 'Issue'
        db.delete_table(u'issues')

        # Deleting model 'Journals'
        db.delete_table(u'journals')

        # Deleting model 'MemberRoles'
        db.delete_table(u'member_roles')

        # Deleting model 'Member'
        db.delete_table(u'members')

        # Deleting model 'Messages'
        db.delete_table(u'messages')

        # Deleting model 'OpenIdAuthenticationNonces'
        db.delete_table(u'open_id_authentication_nonces')

        # Deleting model 'News'
        db.delete_table(u'news')

        # Deleting model 'OpenIdAuthenticationAssociations'
        db.delete_table(u'open_id_authentication_associations')

        # Deleting model 'Project'
        db.delete_table(u'projects')

        # Deleting model 'ProjectsTrackers'
        db.delete_table(u'projects_trackers')

        # Deleting model 'Queries'
        db.delete_table(u'queries')

        # Deleting model 'Repositories'
        db.delete_table(u'repositories')

        # Deleting model 'Roles'
        db.delete_table(u'roles')

        # Deleting model 'SchemaMigrations'
        db.delete_table(u'schema_migrations')

        # Deleting model 'Settings'
        db.delete_table(u'settings')

        # Deleting model 'TimeEntries'
        db.delete_table(u'time_entries')

        # Deleting model 'Tokens'
        db.delete_table(u'tokens')

        # Deleting model 'Trackers'
        db.delete_table(u'trackers')

        # Deleting model 'UserPreferences'
        db.delete_table(u'user_preferences')

        # Deleting model 'User'
        db.delete_table(u'users')

        # Deleting model 'Versions'
        db.delete_table(u'versions')

        # Deleting model 'Watchers'
        db.delete_table(u'watchers')

        # Deleting model 'WikiContentVersions'
        db.delete_table(u'wiki_content_versions')

        # Deleting model 'WikiContents'
        db.delete_table(u'wiki_contents')

        # Deleting model 'WikiPages'
        db.delete_table(u'wiki_pages')

        # Deleting model 'Workflows'
        db.delete_table(u'workflows')

        # Deleting model 'WikiRedirects'
        db.delete_table(u'wiki_redirects')

        # Deleting model 'Wikis'
        db.delete_table(u'wikis')

        # Deleting model 'Changes'
        db.delete_table(u'changes')


    models = {
        'redmine.attachments': {
            'Meta': {'object_name': 'Attachments', 'db_table': "u'attachments'"},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'container_id': ('django.db.models.fields.IntegerField', [], {}),
            'container_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'digest': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'disk_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'downloads': ('django.db.models.fields.IntegerField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'filesize': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'redmine.authsources': {
            'Meta': {'object_name': 'AuthSources', 'db_table': "u'auth_sources'"},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'account_password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'attr_firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'attr_lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'attr_login': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'attr_mail': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'base_dn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'onthefly_register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'port': ('django.db.models.fields.IntegerField', [], {}),
            'tls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'redmine.boards': {
            'Meta': {'object_name': 'Boards', 'db_table': "u'boards'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_message_id': ('django.db.models.fields.IntegerField', [], {}),
            'messages_count': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'topics_count': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.changes': {
            'Meta': {'object_name': 'Changes', 'db_table': "u'changes'"},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'changeset_id': ('django.db.models.fields.IntegerField', [], {}),
            'from_path': ('django.db.models.fields.TextField', [], {}),
            'from_revision': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.changesets': {
            'Meta': {'object_name': 'Changesets', 'db_table': "u'changesets'"},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'commit_date': ('django.db.models.fields.DateField', [], {}),
            'committed_on': ('django.db.models.fields.DateTimeField', [], {}),
            'committer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'repository_id': ('django.db.models.fields.IntegerField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scmid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.changesetsissues': {
            'Meta': {'object_name': 'ChangesetsIssues', 'db_table': "u'changesets_issues'"},
            'changeset_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.comments': {
            'Meta': {'object_name': 'Comments', 'db_table': "u'comments'"},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'commented_id': ('django.db.models.fields.IntegerField', [], {}),
            'commented_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'redmine.customfields': {
            'Meta': {'object_name': 'CustomFields', 'db_table': "u'custom_fields'"},
            'default_value': ('django.db.models.fields.TextField', [], {}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'field_format': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_filter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_for_all': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {}),
            'min_length': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'possible_values': ('django.db.models.fields.TextField', [], {}),
            'regexp': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'searchable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'redmine.customfieldsprojects': {
            'Meta': {'object_name': 'CustomFieldsProjects', 'db_table': "u'custom_fields_projects'"},
            'custom_field_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.customfieldstrackers': {
            'Meta': {'object_name': 'CustomFieldsTrackers', 'db_table': "u'custom_fields_trackers'"},
            'custom_field_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tracker_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.customvalues': {
            'Meta': {'object_name': 'CustomValues', 'db_table': "u'custom_values'"},
            'custom_field_id': ('django.db.models.fields.IntegerField', [], {}),
            'customized_id': ('django.db.models.fields.IntegerField', [], {}),
            'customized_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'redmine.documents': {
            'Meta': {'object_name': 'Documents', 'db_table': "u'documents'"},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'redmine.enabledmodules': {
            'Meta': {'object_name': 'EnabledModules', 'db_table': "u'enabled_modules'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.enumerations': {
            'Meta': {'object_name': 'Enumerations', 'db_table': "u'enumerations'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.groupsusers': {
            'Meta': {'object_name': 'GroupsUsers', 'db_table': "u'groups_users'"},
            'group_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.issue': {
            'Meta': {'object_name': 'Issue', 'db_table': "u'issues'"},
            'assigned_to_id': ('django.db.models.fields.IntegerField', [], {}),
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'done_ratio': ('django.db.models.fields.IntegerField', [], {}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'estimated_hours': ('django.db.models.fields.FloatField', [], {}),
            'fixed_version_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lft': ('django.db.models.fields.IntegerField', [], {}),
            'lock_version': ('django.db.models.fields.IntegerField', [], {}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {}),
            'priority_id': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redmine.Project']"}),
            'rgt': ('django.db.models.fields.IntegerField', [], {}),
            'root_id': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redmine.IssueStatus']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tracker_id': ('django.db.models.fields.IntegerField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'redmine.issuecategories': {
            'Meta': {'object_name': 'IssueCategories', 'db_table': "u'issue_categories'"},
            'assigned_to_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.issuerelations': {
            'Meta': {'object_name': 'IssueRelations', 'db_table': "u'issue_relations'"},
            'delay': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'issue_from_id': ('django.db.models.fields.IntegerField', [], {}),
            'issue_to_id': ('django.db.models.fields.IntegerField', [], {}),
            'relation_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.issuestatus': {
            'Meta': {'object_name': 'IssueStatus', 'db_table': "u'issue_statuses'"},
            'default_done_ratio': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.journaldetails': {
            'Meta': {'object_name': 'JournalDetails', 'db_table': "u'journal_details'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'journal_id': ('django.db.models.fields.IntegerField', [], {}),
            'old_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prop_key': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'property': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.journals': {
            'Meta': {'object_name': 'Journals', 'db_table': "u'journals'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'journalized_id': ('django.db.models.fields.IntegerField', [], {}),
            'journalized_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.member': {
            'Meta': {'object_name': 'Member', 'db_table': "u'members'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'mail_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redmine.Project']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redmine.User']"})
        },
        'redmine.memberroles': {
            'Meta': {'object_name': 'MemberRoles', 'db_table': "u'member_roles'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'inherited_from': ('django.db.models.fields.IntegerField', [], {}),
            'member_id': ('django.db.models.fields.IntegerField', [], {}),
            'role_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.messages': {
            'Meta': {'object_name': 'Messages', 'db_table': "u'messages'"},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'board_id': ('django.db.models.fields.IntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_reply_id': ('django.db.models.fields.IntegerField', [], {}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {}),
            'replies_count': ('django.db.models.fields.IntegerField', [], {}),
            'sticky': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'redmine.news': {
            'Meta': {'object_name': 'News', 'db_table': "u'news'"},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'comments_count': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'redmine.openidauthenticationassociations': {
            'Meta': {'object_name': 'OpenIdAuthenticationAssociations', 'db_table': "u'open_id_authentication_associations'"},
            'assoc_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'issued': ('django.db.models.fields.IntegerField', [], {}),
            'lifetime': ('django.db.models.fields.IntegerField', [], {}),
            'secret': ('django.db.models.fields.TextField', [], {}),
            'server_url': ('django.db.models.fields.TextField', [], {})
        },
        'redmine.openidauthenticationnonces': {
            'Meta': {'object_name': 'OpenIdAuthenticationNonces', 'db_table': "u'open_id_authentication_nonces'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'server_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.project': {
            'Meta': {'object_name': 'Project', 'db_table': "u'projects'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lft': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redmine.Project']"}),
            'rgt': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'redmine.projectstrackers': {
            'Meta': {'object_name': 'ProjectsTrackers', 'db_table': "u'projects_trackers'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'tracker_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.queries': {
            'Meta': {'object_name': 'Queries', 'db_table': "u'queries'"},
            'column_names': ('django.db.models.fields.TextField', [], {}),
            'filters': ('django.db.models.fields.TextField', [], {}),
            'group_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'sort_criteria': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.repositories': {
            'Meta': {'object_name': 'Repositories', 'db_table': "u'repositories'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'root_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.roles': {
            'Meta': {'object_name': 'Roles', 'db_table': "u'roles'"},
            'assignable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'builtin': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'permissions': ('django.db.models.fields.TextField', [], {}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.schemamigrations': {
            'Meta': {'object_name': 'SchemaMigrations', 'db_table': "u'schema_migrations'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'redmine.settings': {
            'Meta': {'object_name': 'Settings', 'db_table': "u'settings'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'redmine.timeentries': {
            'Meta': {'object_name': 'TimeEntries', 'db_table': "u'time_entries'"},
            'activity_id': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'hours': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.IntegerField', [], {}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'spent_on': ('django.db.models.fields.DateField', [], {}),
            'tmonth': ('django.db.models.fields.IntegerField', [], {}),
            'tweek': ('django.db.models.fields.IntegerField', [], {}),
            'tyear': ('django.db.models.fields.IntegerField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.tokens': {
            'Meta': {'object_name': 'Tokens', 'db_table': "u'tokens'"},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'redmine.trackers': {
            'Meta': {'object_name': 'Trackers', 'db_table': "u'trackers'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_in_chlog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_in_roadmap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'users'"},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auth_source_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hashed_password': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'identity_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'last_login_on': ('django.db.models.fields.DateTimeField', [], {}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'mail_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'redmine.userpreferences': {
            'Meta': {'object_name': 'UserPreferences', 'db_table': "u'user_preferences'"},
            'hide_mail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'others': ('django.db.models.fields.TextField', [], {}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.versions': {
            'Meta': {'object_name': 'Versions', 'db_table': "u'versions'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'effective_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'sharing': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {}),
            'wiki_page_title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.watchers': {
            'Meta': {'object_name': 'Watchers', 'db_table': "u'watchers'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'watchable_id': ('django.db.models.fields.IntegerField', [], {}),
            'watchable_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'redmine.wikicontents': {
            'Meta': {'object_name': 'WikiContents', 'db_table': "u'wiki_contents'"},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.wikicontentversions': {
            'Meta': {'object_name': 'WikiContentVersions', 'db_table': "u'wiki_content_versions'"},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'compression': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {}),
            'wiki_content_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.wikipages': {
            'Meta': {'object_name': 'WikiPages', 'db_table': "u'wiki_pages'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wiki_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.wikiredirects': {
            'Meta': {'object_name': 'WikiRedirects', 'db_table': "u'wiki_redirects'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'redirects_to': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wiki_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.wikis': {
            'Meta': {'object_name': 'Wikis', 'db_table': "u'wikis'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'start_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        'redmine.workflows': {
            'Meta': {'object_name': 'Workflows', 'db_table': "u'workflows'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'new_status_id': ('django.db.models.fields.IntegerField', [], {}),
            'old_status_id': ('django.db.models.fields.IntegerField', [], {}),
            'role_id': ('django.db.models.fields.IntegerField', [], {}),
            'tracker_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['redmine']
