from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from .views import AuthComplete


admin.autodiscover()

try:
    admin.site.unregister(Site)
except NotRegistered:
    pass
try:
    admin.site.unregister(User)
except NotRegistered:
    pass

from django.http import HttpResponse
def login_error(request, *args, **kwargs):
    return HttpResponse('LOGIN ERROR!')

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^holiday/', include('holiday.urls')),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^login-error', login_error),
    # url(r'^movie-club/', include('imc.urls')),
    url(r'^shopping-list/', include('status.modules.shoppinglist.urls')),
    url(r'^status/', include('status.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^complete/(?P<backend>[^/]+)/$', AuthComplete.as_view()),
    url(r'', include('social_auth.urls')),
)

urlpatterns += staticfiles_urlpatterns()

