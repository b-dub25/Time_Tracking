from django.contrib.auth.models import (
        User,
        AnonymousUser,
    )
from django.core.exceptions import (
        PermissionDenied,
        ObjectDoesNotExist,
    )
from scheducal.models import (
        WorkEvent, 
        Category,
    )
from pay_period.models import PayPeriod
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.core import serializers
from scheducal.lib.user_helper import user_dict
import datetime
import time

@require_http_methods(['GET'])
def work_event_list_for_pay_period(request, pay_period):
    p = PayPeriod.objects.get(pk=pay_period) 
    if not pay_period:
        raise ObjectDoesNotExist 
    events = []
    for user in User.objects.all():
        try:
            start = p.start
            end = datetime.datetime(year=p.end.year, month=p.end.month, day=p.end.day,
                                    hour=23, minute=59)
            user_events = WorkEvent.objects \
                          .filter(user=user) \
                          .filter(start__gte=start) \
                          .filter(start__lte=end)            
            total = datetime.timedelta()
            durations = [x.duration for x in user_events]
            for i in user_events:
                total = total + i.duration
            events.append({
                'user': user_dict(user),
                'events': [x.to_dict() for x in user_events],
                'total': str(total),
            })
        except Exception as e:
            print e
            return HttpResponse(status=500)

    data = simplejson.dumps(events)
    return HttpResponse(data, mimetype='application/json')
