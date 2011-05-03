from django.conf.urls.defaults import *

urlpatterns = patterns('imc.views',
    url(r'^$', 'index', name='index'),
    url(r'^movie/', 'movie', name='movie'),
)

