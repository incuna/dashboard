from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse


import views

urlpatterns = patterns('holiday.views',
    url(r'^add/$', 'make_holiday_request', name='holiday_make_request'),
    url(r'^(?P<pk>\d+)/$', 'request_details', name='holiday_request_details'),
    url(r'^users/(?P<username>\w+)/$', 'holiday_index', name='holiday_user'),
    url(r'^management/all/$', 'request_inbox', {'show_all':True}, name='holiday_all_pending'),
    url(r'^management/$', 'request_inbox', name='holiday_request_inbox'),
    url(r'^$', 'holiday_index', name='holiday_index'),
    url(r'^users/$', views.EmployeeList.as_view(), name='holiday_employee_list'),
    url(r'^calendar/$', 'holiday_calendar', name='holiday_calendar_view')
)
