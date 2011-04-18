from base64 import b64encode

from django.forms import CharField, ModelForm

from models import Login

class PasswordForm(ModelForm):
    password = CharField(max_length=255)

    class Meta:
        model = Login
        exclude = ('passwd',)

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.initial['password'] = self.instance.password

    def save(self, commit=True):
        model = super(PasswordForm, self).save(commit=True)
        model.passwd = b64encode(self.cleaned_data['password'])

        if commit:
            model.save()
        return model

    def save_m2m(self):
        pass

