from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.http import require_http_methods
from scheducal.lib.user_helper import user_dict

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
    
@require_http_methods(['POST'])
def user_delete(user_id):
    user = User.objects.get(all).filter(user_id.POST['pk'])
    status_code = ""
    try
       user.delete()
       status_code = "201"
    except
       status_code = "400" 
    return HttpResponse(status_code)

@require_http_methods(['POST'])
def create_user(user):    
    status_code =""
    try
       new_user = User()
       new_user.user_name = user.POST['user_name']
       new_user.first_name = user.POST['first_name']
       new_user.last_name = user.POST['last_name']
       new_user.group = user.POST['group'] 
       status_code = "201"
    except
       status_code = "401"
    return HttpResponse(status_code)

@require_http_methods(['POST'])
def update_user(user):
	status_code = "" # default to null string
	updated_user = User().objects(all).filter(user.POST['pk'])
	try:
	   """updated_user.user_name  = user.POST['user_name']
	     updated_user.first_name = user.POST['first_name']
	     updated_user.last_name  = user.POST['last_name']
	     updated_user.group      = user.POST['group']"""
	     modify_user(user)
	   status_code = "201"
	except:
	    status_code = "401" 
	return HttpResponse(status_code)
# One function to rule them all
@require_http_methods(['POST'])
def update_or_create_user(user):
	status_code = ""
	try:
		modify_user(user)
		status_code = "201" # it was a good call
	except:
		status_code = "401" # something bad happened   
	return HttpResponse(status_code)

