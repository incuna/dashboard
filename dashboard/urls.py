from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

try:
    admin.site.unregister(Site)
except NotRegistered:
    pass
try:
    admin.site.unregister(User)
except NotRegistered:
    pass

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^holiday/', include('holiday.urls')),
    url(r'^movie-club/', include('imc.urls')),
    url(r'^shopping-list/', include('status.modules.shoppinglist.urls')),
    url(r'^status/', include('status.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

