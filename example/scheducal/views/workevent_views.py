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
def work_event_list(request):
    work_events = WorkEvent.objects.all()
    data = [work_event.to_dict() for work_event in work_events]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['GET'])
def work_event_list_for_pay_period(request, pay_period):
    pay_period = PayPeriod.objects.get(pk=pay_period) 
    if not pay_period:
        raise ObjectDoesNotExist 
    try:
        events = WorkEvent.objects.filter(start_date__range=[pay_period.start, pay_period.end])
    except:
        raise PermissionDenied

    data = [event.to_dict() for event in events]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['GET'])
def work_event_detail(request, pk):
    event = WorkEvent.objects.get(pk=pk)
    data = simplejson.dumps(event.to_dict())
    return HttpResponse(data, mimetype='application/json') 
