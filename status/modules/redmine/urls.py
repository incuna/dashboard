from django.conf.urls.defaults import *

urlpatterns = patterns('status.modules.redmine.views',
    (r'graphs/', 'graphs'),
    (r'list/', 'list'),
)
