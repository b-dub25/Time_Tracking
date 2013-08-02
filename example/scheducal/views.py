from django.http import HttpResponse
from app.models import User
from django.utils import simplejson
from django.core import serializers

def show_users(request):
    users = User.objects.all()
    data = serializers.serialize('json', users)
    return HttpResponse(data, mimetype='application/json')

def user_detail(request):
    user = User.objects.get(pk=request.POST['pk'])
    data = serializers.serialize('json', user)
    return HttpResponse(data, mimetype'application/json')
