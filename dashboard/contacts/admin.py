from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

from actions import export
from models import Contact

class ContactForm(forms.ModelForm):
    user = forms.ModelChoiceField(required=False, queryset=User.objects.exclude(is_superuser=True))

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        user = cleaned_data.get('user')

        if not name and not user:
            raise forms.ValidationError('Please enter either a Name or a User.')

        return cleaned_data

export.short_description = 'Download'

class ContactAdmin(admin.ModelAdmin):
    actions = [export]
    form = ContactForm

admin.site.register(Contact, ContactAdmin)

