from django.conf.urls.defaults import include, patterns, url

urlpatterns = patterns('status.views',
    url(r'^$', 'index', name='statusboard'),
    url(r'^holiday-cal/', 'todays_holidays', name='todays-holidays'),
    url(r'^redmine/', include('status.modules.redmine.urls')),
    url(r'^weather/', include('status.modules.weather.urls')),
)

