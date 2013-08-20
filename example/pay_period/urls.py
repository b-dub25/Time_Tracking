from django.conf.urls import patterns, url, include
from pay_period import views


urlpatterns = patterns('',
    url(r'^list/$', views.period_list),
    url(r'^add/$', views.period_add),
)
