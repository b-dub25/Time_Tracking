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
from scheducal.views.workevent_views import (
        work_event_list,
        work_event_detail,
        work_event_list_for_pay_period,
        work_event_add,
        work_event_update,
        work_event_delete,
    )
 
urlpatterns = patterns('',
    # User views
    url(r'^user/$', user_list),
    url(r'^user/(?P<pk>[0-9]+)/$', user_detail),

    # Category views
    url(r'^category/$', category_list),
    url(r'^category/(?P<pk>[0-9]+)/$', category_detail),
    url(r'^category/add/$', category_add),

    # Work Event views
    url(r'^workevent/$', work_event_list),
    url(r'^workevent/(?P<pk>[0-9]+)/$', work_event_detail),
    url(r'^workevent/payperiod/(?P<pay_period>[0-9]+)/$', work_event_list_for_pay_period),
    url(r'^workevent/add', work_event_add),
    url(r'^workevent/update/(?P<pk>[0-9]+)/$', work_event_update),
    url(r'^workevent/delete/(?P<pk>[0-9]+)/$', work_event_delete),
)
