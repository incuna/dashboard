import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.dateformat import format

from incuna.utils.mail import render_to_send_mail
from profiles.models import Profile


DATE_FORMAT = '%Y-%m-%d'

if not hasattr(settings,'HOLIDAY_YEAR_START_DAY'):
    settings.HOLIDAY_YEAR_START_DAY = 1
if not hasattr(settings,'HOLIDAY_YEAR_START_MONTH'):
    settings.HOLIDAY_YEAR_START_MONTH = 1


def get_year_start_end(yearoffset=0):
    now = datetime.date.today()
    yearstart = datetime.date(day=settings.HOLIDAY_YEAR_START_DAY, month=settings.HOLIDAY_YEAR_START_MONTH, year=now.year)
    if yearstart > now:
        yearstart = datetime.date(day=yearstart.day, month=yearstart.month, year=yearstart.year-1)
    yearstart = datetime.date(day=yearstart.day, month=yearstart.month, year=yearstart.year+yearoffset)
    yearend = datetime.date(day=yearstart.day, month=yearstart.month, year=yearstart.year+1)
    return yearstart, yearend


# class Employee(User):
#     """An Employee. Extends User by adding details of employment required for calculating holiday."""
#     holiday_per_annum = models.IntegerField(_('annual holiday'), default=settings.HOLIDAY_DEFAULT_ANNUAL_DAYS)
#     start_date = models.DateField(_('start date'))
#     end_date = models.DateField(_('end date'), blank=True, null=True)
#     manager = models.ForeignKey('self', null=True, blank=False, related_name='managed_employees')
#     is_manager = models.BooleanField(_('is manager'), default=False)

#     def accepted_days(self, yearoffset=0):User.objects.all()
#         yearstart, yearend = get_year_start_end(yearoffset)
#         qs = Holiday.objects.filter(holiday_request__employee__exact=self, holiday_request__status__exact=1, date__gte=yearstart, date__lt=yearend).distinct()
#         return qs
        
#     def allowance_days(self, yearoffset=0):
#         yearstart, yearend = get_year_start_end(yearoffset)
#         if  self.start_date > yearstart or (self.end_date and self.end_date < yearend):
#             if self.end_date:
#                 if self.end_date < yearstart:
#                     return 0 #always zero
#                 elif self.end_date < yearend and self.start_date > yearstart:
#                     time_diff = self.end_date - self.start_date
#                 elif self.end_date < yearend:
#                     time_diff = self.end_date - yearstart
#             else: # self.start_date > yearstart:
#                 time_diff = yearend - self.start_date
#             # Added 1 day to the time difference, as you work both your first and last day.
#             # (eg the datedifference of today - yesterday is 1, but you've worked two days)
#             return ((time_diff.days +1) / 365.25) * self.holiday_per_annum
#         else:
#             return self.holiday_per_annum

#     def days_left_count(self, yearoffset=0):
#         alldays = self.accepted_days(yearoffset)
#         days_left = self.allowance_days(yearoffset) - (alldays.count() - (alldays.filter(half_day__exact=True).count() * 0.5))
#         return round(days_left, 2)

#     def pending_requests(self):
#         return HolidayRequest.objects.filter(status__exact=0, employee__exact=self)

#     def managed_pending_requests(self):
#         return HolidayRequest.objects.filter(employee__manager__exact=self, status__exact=0)


class HolidayRequestManager(models.Manager):
    def get_query_set(self):
        return super(HolidayRequestManager, self).get_query_set().annotate(start_date=models.Min('holiday__date'))


class HolidayRequest(models.Model):
    """A Request for holiday/s."""
    PENDING_STATUS = 0
    ACCEPTED_STATUS = 1
    DENIED_STATUS = 2
    STATUS_CHOICES = (
        (PENDING_STATUS,'Pending'),
        (ACCEPTED_STATUS,'Accepted'),
        (DENIED_STATUS,'Denied')
    )
    employee = models.ForeignKey(Profile)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=0)
    date_made = models.DateTimeField(_('request date'), auto_now_add=True)
    administrator = models.ForeignKey(Profile, blank=True, null=True, related_name='admin_set')
    employee_comment = models.TextField(_('Comments'), blank=True, null=True)
    manager_comment  = models.TextField(_('Comments'), blank=True, null=True)

    objects = HolidayRequestManager()

    #class Meta():
    #    ordering = ['-start_date',]

    def start_day(self):
        try:
             return self.holiday_set.all()[0]
        except IndexError:
             return None

    def requested_days(self):
        return Holiday.objects.filter(holiday_request__employee__exact=self.employee, holiday_request__exact=self)

    def days_requested_total(self):
        alldays = self.requested_days()
        return alldays.count() - (alldays.filter(half_day__exact=True).count() * 0.5)

    def days_requested_count(self, yearoffset=0):
        yearstart, yearend = get_year_start_end(yearoffset)
        qs = self.requested_days().filter(date__gte=yearstart, date__lt=yearend)
        return qs.count() - (qs.filter(half_day__exact=True).count() * 0.5)

    def __unicode__(self):
        return u"request for %s days holiday" % (self.days_requested_total())

    def send_request_email(self):
        site = Site.objects.get_current()
        mailextras = {
                     'hol_req': self,
                     'site':site,
                     }
        render_to_send_mail(recipient_list=(self.employee.manager.email,), template='holiday/request_email.txt', extra_context=mailextras, subject='Holiday Request')

    def send_confirmation_email(self):
        site = Site.objects.get_current()
        mailextras = {
                     'hol_req': self,
                     'site':site,
                     }
        render_to_send_mail(recipient_list=(self.employee.email,), template='holiday/confirmation_email.txt', extra_context=mailextras, subject='Re: Holiday Request')

#    def save(self, *args, **kwargs):
#        """
#        Try saving a couple of times (sometimes the google code crashes here :/)
#        """
#        for i in xrange(10):
#            try:
#                super(HolidayRequest, self).save(*args, **kwargs)
#                break
#            except RequestError:
#                pass


class Holiday(models.Model):
    """A holiday to be taken off."""
    holiday_request = models.ForeignKey(HolidayRequest)
    date = models.DateField(_('day off'))
    half_day = models.BooleanField(_('half day'), default=False)

    class Meta():
        ordering = ['date',]

    def __unicode__(self):
        if self.half_day:
            return u"%s (half day)" % (format(self.date,settings.DATE_FORMAT))
        else:
            return u"%s" % (format(self.date,settings.DATE_FORMAT))


class BankHoliday(models.Model):
    """A Bank Holiday. To be excluded from requested holidays"""
    date = models.DateField(_('bank holiday'))
    name = models.CharField(_('name'), default='bank holiday', max_length=255)

    def __unicode__(self):
        return u"%s (%s)" % (self.name, format(self.date,settings.DATE_FORMAT))

    class Meta():
        ordering = ['-date',]

#-------

# Google Calendar integration

#-------

# class HolidayRequestCalendarAdapter(CalendarAdapter):
#     """
#     A Calendar Adapter for the Holiday model
#     """
#     def get_event_data(self, instance):
#         """
#         Returns a CalendarEventData object filled with data from the HolidayRequest instance.
#         """
#         holiday_set = list(instance.holiday_set.all())
#         first_hol = holiday_set[0].date
#         last_hol  = holiday_set[-1].date + datetime.timedelta(days=1)
#         start = datetime.datetime(year=first_hol.year,month=first_hol.month,day=first_hol.day)
#         end   = datetime.datetime(year=last_hol.year, month=last_hol.month, day=last_hol.day)

#         title = u"%s holiday" %(instance.employee.get_full_name())
#         half_days = 0

#         content = u""
#         if instance.employee_comment:
#             content+= u"%s commented: %s\n\n" %(instance.employee.get_full_name(), instance.employee_comment)
#         if instance.manager_comment:
#             content+= u"%s commented: %s\n\n" %(instance.administrator.get_full_name(), instance.manager_comment)

#         for day in holiday_set:
#             content += u"%s\n" %(day)
#             if day.half_day:
#                 half_days += 1

#         if half_days:
#             title += u" ("
#             if half_days != len(holiday_set):
#                 title += u"inc "
#             title += u"%d Half Day%s)" % (half_days, "s" if half_days>1 else "")

#         content = Content(text=content)
#         title = Title(text=title)
#         when = [When(
#                     start_time= start.strftime(DATE_FORMAT),
#                     end_time  = end.strftime(DATE_FORMAT)
#                     )]

#         return RawCalendarEventData(
#                                    when    = when,
#                                    title   = title,
#                                    content = content,
#                                    )

#     def can_save(self, instance):
#         return instance.status == 1 and instance.holiday_set.count() > 0
#         #return True

# holiday_request_observer = CalendarObserver(email=settings.HOLIDAY_CALENDAR_EMAIL,
#                                     password=settings.HOLIDAY_CALENDAR_PASSWORD)
# holiday_request_observer.observe(HolidayRequest, HolidayRequestCalendarAdapter())
