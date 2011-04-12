from django.db import models

class Password(models.Model):
    password = models.CharField(max_length=255)
    username = models.ForeignKey('Login')

    def __unicode__(self):
        return self.username

class Login(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.domain)

