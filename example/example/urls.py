from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('example.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('scheducal.urls')),
    url(r'^', include('pay_period.urls')),
    url(r'^$', 'api_root'),
    url(r'^auth/', include('tokenauth.urls')),
    url(r'^request/', include('faculty_request.urls')),
    url(r'^inventory/', include('Inventory_Management.urls')),
)
