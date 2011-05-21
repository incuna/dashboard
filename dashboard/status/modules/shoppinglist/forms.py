from django import forms

from models import Item

class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Item

    def save(self, commit=False):
        instance = super(ItemAdminForm, self).save(commit=commit)
        if not instance.pk and not self.current_user.is_superuser:
            if not self.current_user.profile.is_manager:
                instance.added_by = self.current_user.profile
        instance.save()
        return instance

