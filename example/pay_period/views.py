from django.http import HttpResponse
from pay_period.models import PayPeriod
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def list(request):
    periods = [period.to_dict() for period in PayPeriod.objects.all()]
    data = {'message': '', 'pay_periods': periods}
    data = simplejson.dumps(data)
    return HttpResponse(data, status=200)

@csrf_exempt
def add(request):
    try:
        PayPeriod(
            name=request.POST['name'],
            start=request.POST['start'],
            end=request.POST['end']).save()
        data = {'message': 'cool'}
        data = simplejson.dumps(data)
    except:
        data = {'message': 'Failure saving Pay Period'}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=403)
    return HttpResponse(data, status=201)
