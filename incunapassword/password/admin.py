from django.contrib import admin

from forms import PasswordForm
from models import Login, Password

class PasswordInline(admin.TabularInline):
    model = Password
    extra = 0
    form = PasswordForm

class LoginAdmin(admin.ModelAdmin):
    inlines = [PasswordInline]

admin.site.register(Login, LoginAdmin)

