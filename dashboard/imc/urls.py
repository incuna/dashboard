from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('imc.views',
    url(r'^$', 'index', name='index'),
    url(r'^movie/', 'movie', name='movie'),
    url(r'^dvd-request/(.*)/', 'dvd_request', name='dvd-request'),
)

