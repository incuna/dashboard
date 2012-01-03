from django.contrib import admin

from forms import ItemAdminForm
from models import Item

class ItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    fields = ('name', 'description')
    list_display = ('name', 'created', 'bought')
    list_editable = ['bought']
    list_filter = ['created', 'bought']
    ordering = ['created']

    form = ItemAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(ItemAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            if not request.user.profile.is_manager:
                self.exclude = ('added_by',)
        form.current_user = request.user
        return form

admin.site.register(Item, ItemAdmin)

