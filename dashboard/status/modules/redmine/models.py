# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

from managers import IssueManager, ProjectManager

class Attachments(models.Model):
    id = models.IntegerField(primary_key=True)
    container_id = models.IntegerField()
    container_type = models.CharField(max_length=30)
    filename = models.CharField(max_length=255)
    disk_filename = models.CharField(max_length=255)
    filesize = models.IntegerField()
    content_type = models.CharField(max_length=255)
    digest = models.CharField(max_length=40)
    downloads = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateTimeField()
    description = models.CharField(max_length=255)
    class Meta:
        db_table = u'attachments'

class Boards(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    position = models.IntegerField()
    topics_count = models.IntegerField()
    messages_count = models.IntegerField()
    last_message_id = models.IntegerField()
    class Meta:
        db_table = u'boards'

class AuthSources(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    host = models.CharField(max_length=60)
    port = models.IntegerField()
    account = models.CharField(max_length=255)
    account_password = models.CharField(max_length=60)
    base_dn = models.CharField(max_length=255)
    attr_login = models.CharField(max_length=30)
    attr_firstname = models.CharField(max_length=30)
    attr_lastname = models.CharField(max_length=30)
    attr_mail = models.CharField(max_length=30)
    onthefly_register = models.BooleanField()
    tls = models.BooleanField()
    class Meta:
        db_table = u'auth_sources'

class Changesets(models.Model):
    id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField()
    revision = models.CharField(max_length=255)
    committer = models.CharField(max_length=255)
    committed_on = models.DateTimeField()
    comments = models.TextField()
    commit_date = models.DateField()
    scmid = models.CharField(max_length=255)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'changesets'

class ChangesetsIssues(models.Model):
    changeset_id = models.IntegerField()
    issue_id = models.IntegerField()
    class Meta:
        db_table = u'changesets_issues'

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    commented_type = models.CharField(max_length=30)
    commented_id = models.IntegerField()
    author_id = models.IntegerField()
    comments = models.TextField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    class Meta:
        db_table = u'comments'

class CustomFields(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    field_format = models.CharField(max_length=30)
    possible_values = models.TextField()
    regexp = models.CharField(max_length=255)
    min_length = models.IntegerField()
    max_length = models.IntegerField()
    is_required = models.BooleanField()
    is_for_all = models.BooleanField()
    is_filter = models.BooleanField()
    position = models.IntegerField()
    searchable = models.BooleanField()
    default_value = models.TextField()
    editable = models.BooleanField()
    class Meta:
        db_table = u'custom_fields'

class CustomFieldsProjects(models.Model):
    custom_field_id = models.IntegerField()
    project_id = models.IntegerField()
    class Meta:
        db_table = u'custom_fields_projects'

class CustomFieldsTrackers(models.Model):
    custom_field_id = models.IntegerField()
    tracker_id = models.IntegerField()
    class Meta:
        db_table = u'custom_fields_trackers'

class EnabledModules(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'enabled_modules'

class CustomValues(models.Model):
    id = models.IntegerField(primary_key=True)
    customized_type = models.CharField(max_length=30)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.TextField()
    class Meta:
        db_table = u'custom_values'

class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'documents'

class Enumerations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.IntegerField()
    is_default = models.BooleanField()
    type = models.CharField(max_length=255)
    active = models.BooleanField()
    project_id = models.IntegerField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'enumerations'

class GroupsUsers(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = u'groups_users'

class IssueCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=30)
    assigned_to_id = models.IntegerField()
    class Meta:
        db_table = u'issue_categories'

class IssueRelations(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_from_id = models.IntegerField()
    issue_to_id = models.IntegerField()
    relation_type = models.CharField(max_length=255)
    delay = models.IntegerField()
    class Meta:
        db_table = u'issue_relations'

class IssueStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    is_closed = models.BooleanField()
    is_default = models.BooleanField()
    position = models.IntegerField()
    default_done_ratio = models.IntegerField()

    class Meta:
        db_table = u'issue_statuses'

    def __unicode__(self):
        return self.name

class Issue(models.Model):
    id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    project = models.ForeignKey('Project')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    category_id = models.IntegerField()
    status = models.ForeignKey('IssueStatus')
    assigned_to = models.ForeignKey('User')
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField()
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    start_date = models.DateField()
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField()
    parent_id = models.IntegerField()
    root_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()

    objects = IssueManager()

    class Meta:
        db_table = u'issues'

    def __unicode__(self):
        return 'Issue %s: %s' % (self.id, self.subject)

class Journal(models.Model):
    id = models.IntegerField(primary_key=True)
    journalized_id = models.IntegerField()
    journalized_type = models.CharField(max_length=30)
    user = models.ForeignKey('User')
    notes = models.TextField()
    created_on = models.DateTimeField()

    class Meta:
        db_table = u'journals'

    def __unicode__(self):
        return '%s: %s' % (self.id, self.user.firstname)

class JournalDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    journal = models.ForeignKey('Journal')
    property = models.CharField(max_length=30)
    prop_key = models.CharField(max_length=30)
    old_value = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = u'journal_details'

    def __unicode__(self):
        return '%s (%s): %s => %s' % (self.id, self.journal.id, self.old_value, self.value)

class MemberRoles(models.Model):
    id = models.IntegerField(primary_key=True)
    member_id = models.IntegerField()
    role_id = models.IntegerField()
    inherited_from = models.IntegerField()
    class Meta:
        db_table = u'member_roles'

# Join table for projects - users
class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User')
    project = models.ForeignKey('Project')
    created_on = models.DateTimeField()
    mail_notification = models.BooleanField()

    class Meta:
        db_table = u'members'

    def __unicode__(self):
        return '%s: %s %s' % (self.id, self.user.firstname, self.user.lastname)

class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    board_id = models.IntegerField()
    parent_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    author_id = models.IntegerField()
    replies_count = models.IntegerField()
    last_reply_id = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    locked = models.BooleanField()
    sticky = models.IntegerField()
    class Meta:
        db_table = u'messages'

class OpenIdAuthenticationNonces(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.IntegerField()
    server_url = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    class Meta:
        db_table = u'open_id_authentication_nonces'

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    author_id = models.IntegerField()
    created_on = models.DateTimeField()
    comments_count = models.IntegerField()
    class Meta:
        db_table = u'news'

class OpenIdAuthenticationAssociations(models.Model):
    id = models.IntegerField(primary_key=True)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    handle = models.CharField(max_length=255)
    assoc_type = models.CharField(max_length=255)
    server_url = models.TextField() # This field type is a guess.
    secret = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'open_id_authentication_associations'

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    homepage = models.CharField(max_length=255)
    is_public = models.BooleanField()
    parent = models.ForeignKey('self', null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    identifier = models.CharField(max_length=20)
    status = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()

    objects = ProjectManager()

    class Meta:
        db_table = u'projects'

    def __unicode__(self):
        return 'Project %s: %s' % (self.id, self.name)

class ProjectsTrackers(models.Model):
    project_id = models.IntegerField()
    tracker_id = models.IntegerField()
    class Meta:
        db_table = u'projects_trackers'

class Queries(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    filters = models.TextField()
    user_id = models.IntegerField()
    is_public = models.BooleanField()
    column_names = models.TextField()
    sort_criteria = models.TextField()
    group_by = models.CharField(max_length=255)
    class Meta:
        db_table = u'queries'

class Repositories(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    url = models.CharField(max_length=255)
    login = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    root_url = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    class Meta:
        db_table = u'repositories'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.IntegerField()
    assignable = models.BooleanField()
    builtin = models.IntegerField()
    permissions = models.TextField()
    class Meta:
        db_table = u'roles'

class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'schema_migrations'

class Settings(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField()
    updated_on = models.DateTimeField()
    class Meta:
        db_table = u'settings'

class TimeEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField()
    hours = models.FloatField()
    comments = models.CharField(max_length=255)
    activity_id = models.IntegerField()
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    class Meta:
        db_table = u'time_entries'

class Tokens(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    action = models.CharField(max_length=30)
    value = models.CharField(max_length=40)
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'tokens'

class Trackers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    is_in_chlog = models.BooleanField()
    position = models.IntegerField()
    is_in_roadmap = models.BooleanField()
    class Meta:
        db_table = u'trackers'

class UserPreferences(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    others = models.TextField()
    hide_mail = models.BooleanField()
    time_zone = models.CharField(max_length=255)
    class Meta:
        db_table = u'user_preferences'

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=30)
    hashed_password = models.CharField(max_length=40)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mail = models.CharField(max_length=60)
    mail_notification = models.BooleanField()
    admin = models.BooleanField()
    status = models.IntegerField()
    last_login_on = models.DateTimeField()
    language = models.CharField(max_length=5)
    auth_source_id = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    type = models.CharField(max_length=255)
    identity_url = models.CharField(max_length=255)

    class Meta:
        db_table = u'users'

    def __unicode__(self):
        return '%s: %s %s' % (self.id, self.firstname, self.lastname)

class Versions(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    effective_date = models.DateField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    wiki_page_title = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    sharing = models.CharField(max_length=255)
    class Meta:
        db_table = u'versions'

class Watchers(models.Model):
    id = models.IntegerField(primary_key=True)
    watchable_type = models.CharField(max_length=255)
    watchable_id = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = u'watchers'

class WikiContentVersions(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_content_id = models.IntegerField()
    page_id = models.IntegerField()
    author_id = models.IntegerField()
    data = models.TextField() # This field type is a guess.
    compression = models.CharField(max_length=6)
    comments = models.CharField(max_length=255)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        db_table = u'wiki_content_versions'

class WikiContents(models.Model):
    id = models.IntegerField(primary_key=True)
    page_id = models.IntegerField()
    author_id = models.IntegerField()
    text = models.TextField()
    comments = models.CharField(max_length=255)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        db_table = u'wiki_contents'

class WikiPages(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    protected = models.BooleanField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'wiki_pages'

class Workflows(models.Model):
    id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    old_status_id = models.IntegerField()
    new_status_id = models.IntegerField()
    role_id = models.IntegerField()
    class Meta:
        db_table = u'workflows'

class WikiRedirects(models.Model):
    id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=255)
    redirects_to = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'wiki_redirects'

class Wikis(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    start_page = models.CharField(max_length=255)
    status = models.IntegerField()
    class Meta:
        db_table = u'wikis'

class Changes(models.Model):
    id = models.IntegerField(primary_key=True)
    changeset_id = models.IntegerField()
    action = models.CharField(max_length=1)
    path = models.TextField()
    from_path = models.TextField()
    from_revision = models.CharField(max_length=255)
    revision = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    class Meta:
        db_table = u'changes'
