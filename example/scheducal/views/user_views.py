from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.http import require_http_methods

def user_dict(user):
    groups = [group.pk for group in user.groups.all()]
    return {
        'id': user.pk,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'groups': groups or None,
    }
    
@require_http_methods(['GET'])
def user_list(request):
    users = User.objects.all()
    data = [user_dict(user) for user in users]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['GET'])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    data = simplejson.dumps(user_dict(user))
    return HttpResponse(data, mimetype='application/json')
