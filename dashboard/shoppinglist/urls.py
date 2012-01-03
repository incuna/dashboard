from django.conf.urls.defaults import patterns, url

from shoppinglist.views import Index, Json


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='item-list'),
    url(r'^json/$', Json.as_view(), name='json'),
)

