from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from holiday.models import Holiday, HolidayRequest, get_year_start_end


def _accepted_days(self, yearoffset=0):
    yearstart, yearend = get_year_start_end(yearoffset)
    qs = Holiday.objects.filter(holiday_request__employee__exact=self, holiday_request__status__exact=1, date__gte=yearstart, date__lt=yearend).distinct()
    return qs
    
def _allowance_days(self, yearoffset=0):
    yearstart, yearend = get_year_start_end(yearoffset)
    if  self.start_date > yearstart or (self.end_date and self.end_date < yearend):
        if self.end_date:
            if self.end_date < yearstart:
                return 0 #always zero
            elif self.end_date < yearend and self.start_date > yearstart:
                time_diff = self.end_date - self.start_date
            elif self.end_date < yearend:
                time_diff = self.end_date - yearstart
        else: # self.start_date > yearstart:
            time_diff = yearend - self.start_date
        # Added 1 day to the time difference, as you work both your first and last day.
        # (eg the datedifference of today - yesterday is 1, but you've worked two days)
        return ((time_diff.days +1) / 365.25) * self.holiday_per_annum
    else:
        return self.holiday_per_annum

def _days_left_count(self, yearoffset=0):
    alldays = self.accepted_days(yearoffset)
    days_left = self.allowance_days(yearoffset) - (alldays.count() - (alldays.filter(half_day__exact=True).count() * 0.5))
    return round(days_left, 2)

def _pending_requests(self):
    return HolidayRequest.objects.filter(status__exact=0, employee__exact=self)

def _managed_pending_requests(self):
    return HolidayRequest.objects.filter(employee__manager__exact=self, status__exact=0)


def register(cls, admin_cls):
    cls.add_to_class('holiday_per_annum', models.IntegerField(_('annual holiday'), default=settings.HOLIDAY_DEFAULT_ANNUAL_DAYS))
    cls.add_to_class('start_date', models.DateField(_('start date')))
    cls.add_to_class('end_date', models.DateField(_('end date'), blank=True, null=True))
    cls.add_to_class('manager', models.ForeignKey('self', null=True, blank=False, related_name='managed_employees'))
    cls.add_to_class('accepted_days', _accepted_days)
    cls.add_to_class('allowance_days', _allowance_days)
    cls.add_to_class('days_left_count', _days_left_count)
    cls.add_to_class('pending_requests', _pending_requests)
    cls.add_to_class('managed_pending_requests', _managed_pending_requests)


    if admin_cls:
        if admin_cls.fieldsets:
            admin_cls.fieldsets.append(
                (_('Holidays'), { 'fields': ('holiday_per_annum', 'start_date', 'end_date'), 'classes': ('collapse',)})
            )

