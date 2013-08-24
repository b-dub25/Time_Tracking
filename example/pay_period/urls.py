from django.conf.urls import patterns, url, include
from pay_period import views


urlpatterns = patterns('',
    url(r'^list/$', views.list),
    url(r'^add/$', views.add),
)
