from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(User)

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
