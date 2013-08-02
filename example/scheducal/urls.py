from django.conf.urls import (
        patterns, 
        url, 
        include,
    )
from scheducal.views import ()
 
urlpatterns = patterns('scheducal.views',
    url(r'^users/$', 'user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', 'user_detail'),
)
