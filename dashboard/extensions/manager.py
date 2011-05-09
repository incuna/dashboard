from django.db import models

def register(cls, admin_cls):
    cls.add_to_class('is_manager', models.BooleanField())

    if admin_cls:
        if admin_cls.fieldsets:
            fields = admin_cls.fieldsets[1][1]['fields']
            try:
                at = fields.index('is_active') + 1
            except ValueError:
                at = len(fields)
            fields.insert(at, 'is_manager')

