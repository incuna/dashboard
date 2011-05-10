from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('status.modules.weather.views',
    url(r'', 'index'),
)
