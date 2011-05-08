from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from services.identity.api import IdentifierResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v0_api = Api(api_name='v0')
v0_api.register(IdentifierResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'services.views.home', name='home'),
    # url(r'^services/', include('services.foo.urls')),

    url(r'^api/', include(v0_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
