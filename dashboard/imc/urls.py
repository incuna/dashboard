from django.conf.urls.defaults import patterns, url

from imc.views import PreviousMovieListView

urlpatterns = patterns('imc.views',
    url(r'^$', 'index', name='movie-index'),
    url(r'^current/$', 'current', name='movie-current'),
    url(r'^group/$', 'group_rating', name='movie-group-rating'),
    url(r'^previous/$', PreviousMovieListView.as_view(), name='movie-previous'),
    url(r'^submit/$', 'submit', name='movie-submit'),
    url(r'^widget/$', 'widget', name='movie-widget'),
    url(r'^(?P<slug>.*)/$', 'movie', name='movie'),
)

