from django.conf.urls.defaults import patterns, url

from shoppinglist.views import Json


urlpatterns = patterns('',
    url(r'^json/$', Json.as_view(), name='json'),
)

