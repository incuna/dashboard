from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView

from imc.models import Movie
from imc.views import Current, Index, PreviousMovie, SubmitMovie

urlpatterns = patterns('imc.views',
    url(r'^$', Index.as_view(), name='movie-index'),
    url(r'^current/$', Current.as_view(), name='movie-current'),
    url(r'^group/$', 'group_rating', name='movie-group-rating'),
    url(r'^previous/$', PreviousMovie.as_view(), name='movie-previous'),
    url(r'^submit/$', SubmitMovie.as_view(), name='movie-submit'),
    url(r'^widget/$', 'widget', name='movie-widget'),
    url(r'^(?P<slug>.*)/$', DetailView.as_view(model=Movie), name='movie'),
)

