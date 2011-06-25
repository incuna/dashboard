from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('imc.views',
    url(r'^$', 'index', name='movie-index'),
    url(r'^current/$', 'current', name='movie-current'),
    url(r'^group/$', 'group', name='movie-group-rating'),
    url(r'^submit/$', 'current', name='movie-submit'),
    url(r'^widget/$', 'widget', name='movie-widget'),
    url(r'^(?P<slug>.*)/$', 'movie', name='movie'),
)

