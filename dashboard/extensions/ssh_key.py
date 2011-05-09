from django.db import models
from django.utils.translation import ugettext_lazy as _

def register(cls, admin_cls):
    cls.add_to_class('ssh_key', models.TextField('SSH Key', blank=True, null=True,
        help_text='Paste the user\'s public key in here. On a Mac you can get this with: "cat ~/.ssh/id_rsa.pub | pbcopy" which copies it to your clipboard.'))

    if admin_cls:
        if admin_cls.fieldsets:
            admin_cls.fieldsets.append(
                (_('SSH Access'), { 'fields': ('ssh_key',), 'classes': ('collapse',)})
            )

