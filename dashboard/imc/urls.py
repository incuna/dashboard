from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('imc.views',
    url(r'^$', 'current', name='current'),
    url(r'^dvd-request/(.*)/', 'dvd_request', name='dvd-request'),
    url(r'^widget/$', 'widget', name='widget'),
    url(r'^(?P<slug>.*)/$', 'movie', name='movie'),
)

