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
    '''
    list work events for logged in user
    '''
    if not request.user:
        return HttpResponse(status=403)
    work_events = WorkEvent.objects.filter(user=request.user)
    data = [work_event.to_dict() for work_event in work_events]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['GET'])
def work_event_list_for_pay_period(request, pay_period):
    pay_period = PayPeriod.objects.get(pk=pay_period) 
    user = request.user
    if not user:
        raise PermissionDenied
    if not pay_period:
        raise ObjectDoesNotExist 
    try:
        events = WorkEvent.objects.filter(user=user,start__range=[pay_period.start, pay_period.end])
    except:
        data = {'message': 'Error filtering by pay period'}
        return HttpResponse(data, status=500)

    data = [event.to_dict() for event in events]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['GET'])
def work_event_detail(request, pk):
    event = WorkEvent.objects.get(pk=pk)
    data = simplejson.dumps(event.to_dict())
    return HttpResponse(data, mimetype='application/json') 

@csrf_exempt
@require_http_methods(['POST'])
def work_event_create(request):
    clocked_in = request.POST['clocked_in']
    if clocked_in == 'True' or clocked_in == 'true' or clocked_in == True:
        clocked_in = True
    else:
        clocked_in = False
    data = simplejson.dumps({'message': ''})
    try:
        work_event = WorkEvent(#**request.POST)
                        user=request.user,
                        start_time=request.POST['start_time'],
                        end_time=request.POST['end_time'],
                        start_date=request.POST['start_date'],
                        comments=request.POST['comments'],
                        categoty=request.POST['category'],
                        clocked_in=clocked_in)
    except:
        return HttpResponse(data, status=400)
    return HttpResponse(data, status=201, mimetype='application/json')
    
@csrf_exempt
@require_http_methods(['POST'])
def work_event_update(request, pk):
    clocked_in = request.POST['clocked_in']
    if clocked_in == 'True' or clocked_in == 'true' or clocked_in == True:
        clocked_in = True
    else:
        clocked_in = False
    workevent = WorkEvent.objects.get(pk=pk)
    workevent.start_time = request.POST['start_time']
    workevent.end_time = request.POST['end_time']
    workevent.start_date = request.POST['start_date']
    workevent.comments = request.POST['comments']
    workevent.category = Category.objects.get(pk=request.POST['category'])
    workevent.clocked_in = clocked_in

    try:
        workevent.save()
        data = {'data': 'Work Event Updated'}
        code = 200
    except Exception as e:
        print e
        data = {'message': 'Work Event Update Failed'}
        code = 400
    return HttpResponse(simplejson.dumps(data), status=code)

@csrf_exempt
@require_http_methods(['POST'])
def work_event_delete(request, pk):
    workevent = WorkEvent.objects.get(pk=pk)

    try:
        workevent.delete()
        data = {'data': 'Work Event Deleted'}
        code = 200
    except:
        data = {'message': 'Work Event Deletion Failed'}
        code = 400
    return HttpResponse(simplejson.dumps(data), status=code)
