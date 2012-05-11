from django.conf.urls.defaults import patterns, url


import views

urlpatterns = patterns('holiday.views',
    url(r'^$', 'holiday_index', name='holiday_index'),
    url(r'^add/$', 'make_holiday_request', name='holiday_make_request'),
    url(r'^calendar/$', views.HolidayCalendar.as_view(), name='holiday_calendar_view')
    url(r'^management/all/$', views.AllPendingRequestsList.as_view(), name='holiday_all_pending'),
    url(r'^management/$', views.PendingRequestsList.as_view(), name='holiday_request_inbox'),
    url(r'^users/$', views.EmployeeList.as_view(), name='holiday_employee_list'),
    url(r'^users/(?P<username>\w+)/$', 'holiday_index', name='holiday_user'),
    url(r'^(?P<pk>\d+)/$', 'request_details', name='holiday_request_details'),
)
