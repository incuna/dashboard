from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    url(r'^movie-club/', include('imc.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

