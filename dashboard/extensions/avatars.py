from django.db import models
from django.utils.translation import ugettext_lazy as _

def register(cls, admin_cls):
    cls.add_to_class('avatar', models.ImageField('Avatar', upload_to='images/avatars'))
    cls.add_to_class('posh_avatar', models.ImageField('Posh Avatar', upload_to='images/avatars/posh',
                    null=True, blank=True, help_text='Use this to provide a work avatar'))

    if admin_cls:
        if admin_cls.fieldsets:
            admin_cls.fieldsets.append(
                (_('Pictures'), { 'fields': ('avatar', 'posh_avatar'), 'classes': ('collapse',)})
            )

