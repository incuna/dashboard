from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)
admin.site.unregister(User)

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^movie-club/', include('imc.urls')),
    url(r'^shopping-list/', include('status.modules.shoppinglist.urls')),
    url(r'^status/', include('status.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

