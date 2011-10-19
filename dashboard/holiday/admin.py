from django.contrib import admin
from django import forms
from incuna.forms import PlainPasswordUserForm
from holiday.models import HolidayRequest, Holiday, BankHoliday



# class EmployeeForm(PlainPasswordUserForm):
#     manager = forms.ModelChoiceField(queryset=Employee.objects.filter(is_manager=True))

#     class Meta:
#         model = Employee

#     def clean_username(self):
#         return self.cleaned_data["username"].lower()


# class EmployeeAdmin(admin.ModelAdmin):
#     def days_left_this_year(self, obj):
#         return obj.days_left_count(0)

#     def days_left_next_year(self, obj):
#         return obj.days_left_count(1)

#     form = EmployeeForm
#     fieldsets =(
#         (None, {
#             'fields': (
#                 'username',
#                 'email',
#                 'first_name',
#                 'last_name',
#                 'plain_password',
#                 'password',
#                 'holiday_per_annum',
#                 'start_date',
#                 'end_date',
#                 'manager',
#             )
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_manager',
#                 'is_staff',
#                 'is_superuser',
#                 'is_active',
#                 'groups',
#                 'user_permissions',
#             ),
#             'classes': ('collapse',)
#         }),
#     )
#     list_display = (
#         'username',
#         'first_name',
#         'last_name',
#         'start_date',
#         'end_date',
#         'manager',
#         'holiday_per_annum',
#         'days_left_this_year',
#         'days_left_next_year',
#         'is_manager',
#         'is_staff',
#         'is_superuser'
#     )
#     list_display_links = ('username',)
#     search_fields = ('email',  'first_name', 'last_name')


class HolidayInline(admin.TabularInline):
    model = Holiday


class HolidayRequestAdmin(admin.ModelAdmin):
    list_display = ('employee','status','date_made','start_day',)
    inlines = [HolidayInline,]
    date_hierarchy = 'date_made'
    list_filter = ['employee','status','administrator',]


class BankHolidayAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    date_hierarchy = 'date'


#admin.site.register(Employee, EmployeeOptions)
admin.site.register(HolidayRequest,HolidayRequestAdmin)
admin.site.register(Holiday)
admin.site.register(BankHoliday, BankHolidayAdmin)
