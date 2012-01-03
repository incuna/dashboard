from django.db import models

from profiles.models import Profile

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    bought = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(Profile)

    def __unicode__(self):
        return self.name

    bought.short_description = 'Bought?'

