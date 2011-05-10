from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('status.modules.shoppinglist.views',
    url(r'', 'index'),
)
