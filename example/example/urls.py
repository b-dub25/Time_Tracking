from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('example.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('scheducal.urls')),
    url(r'^payperiod/^', include('pay_period.urls')),
    url(r'^auth/', include('tokenauth.urls')),
)
