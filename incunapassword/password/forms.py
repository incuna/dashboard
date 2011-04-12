from django.forms import CharField, ModelForm, PasswordInput

from models import Password

class PasswordForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = Password

