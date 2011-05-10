from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=255)
    bought = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    bought.short_description = 'Bought?'

