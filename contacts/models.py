from django.db import models

from profiles.models import Profile

class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Optional: If a User is picked and no name given, one will be generated.')
    user = models.OneToOneField(Profile, null=True)
    extension = models.CharField(max_length=7)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if self.name == '':
            self.name = self.user.first_name
        super(Contact, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

