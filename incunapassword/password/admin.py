from django.contrib import admin

from forms import PasswordForm
from models import Login

class LoginAdmin(admin.ModelAdmin):
    form = PasswordForm
    search_fields = ['name', 'username', 'domain']

admin.site.register(Login, LoginAdmin)

