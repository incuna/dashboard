from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('imc.views',
    url(r'^$', 'movie', name='current'),
    url(r'^(?P<slug>.*)/$', 'movie', name='movie'),
    #url(r'^dvd-request/(.*)/', 'dvd_request', name='dvd-request'),
    url(r'^widget/$', 'widget', name='widget'),
)

