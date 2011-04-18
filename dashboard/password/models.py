from base64 import b64decode

from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True)
    passwd = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.domain)

    @property
    def password(self):
        return b64decode(self.passwd)

