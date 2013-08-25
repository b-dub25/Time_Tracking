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

@require_http_methods(['GET'])
def work_event_list_for_pay_period(request, pay_period):
    pay_period = PayPeriod.objects.get(pk=pay_period) 
    if not pay_period:
        raise ObjectDoesNotExist 
    events = []
    for user in User.objects.all():
        try:
            user_events = WorkEvent.objects \
                          .filter(start_date__range=[pay_period.start, \
                                                     pay_period.end])            
            user_events = [event.to_dict() for event in user_events]
            events.append({
                'user': user,
                'events': user_events,
            })
        except: pass

    data = simplejson.dumps(events)
    return HttpResponse(data, mimetype='application/json')
