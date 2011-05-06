from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)
admin.site.unregister(User)

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    url(r'^movie-club/', include('imc.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

