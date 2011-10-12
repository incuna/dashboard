from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
