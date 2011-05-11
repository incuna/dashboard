from django.conf.urls.defaults import include, patterns, url

urlpatterns = patterns('status.views',
    url(r'^$', 'index', name='statusboard'),
    url(r'^holidaycal/', 'todays_holidays', name='todays-holidays'),
    url(r'^redmine/', include('status.modules.redmine.urls')),
    url(r'^shoppinglist/', include('status.modules.shoppinglist.urls')),
    url(r'^weather/', include('status.modules.weather.urls')),

    url(r'^twitterstream/', include('twitterstream.urls')),
)

