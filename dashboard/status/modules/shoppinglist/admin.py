from django.contrib import admin

from models import Item

class ItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    fields = ('name', 'description')
    list_display = ('name', 'created', 'bought')
    list_editable = ['bought']
    list_filter = ['created', 'bought']
    ordering = ['created']

admin.site.register(Item, ItemAdmin)

