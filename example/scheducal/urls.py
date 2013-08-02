from django.conf.urls import (
        patterns, 
        url, 
        include,
    )
from scheducal.views.user_views import (
        user_list,
        user_detail,
    )
from scheducal.views.category_views import (
        category_list,
        category_detail,
        category_add,
    )
 
urlpatterns = patterns('',
    # User views
    url(r'^user/$', user_list),
    url(r'^user/(?P<pk>[0-9]+)/$', user_detail),

    #Category views
    url(r'^category/$', category_list),
    url(r'^category/(?P<pk>[0-9]+)/$', category_detail),
    url(r'^category/add/$', category_add),
)
