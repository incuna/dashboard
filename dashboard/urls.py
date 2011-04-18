from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'password.views.index', name='index'),
    #url(r'^search/', 'password.views.search', name='search'),
    #url(r'^name/', 'password.views.name', name='name'),
    #url(r'^username/', 'password.views.username', name='username'),
    #url(r'^domain/', 'password.views.domain', name='domain'),

    url(r'^admin/', include(admin.site.urls)),
)
