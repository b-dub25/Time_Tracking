def user_dict(user):
    groups = [group.pk for group in user.groups.all()]
    return {
        'id': user.pk,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'groups': groups or None,
        'email': user.email,
    }
@require_http_methods(['POST'])
def modify_user(user):
	if User().objects.get(all).filter(user.POST['pk']).exists():
		updated_user = User().objects.get(all).filter(user.POST['pk'])
		updated_user.user_name  = user.POST['user_name']
	    updated_user.first_name = user.POST['first_name']
	    updated_user.last_name  = user.POST['last_name']
	    updated_user.group      = user.POST['group']
    else:
	    new_user = User()
        new_user.user_name = user.POST['user_name']
        new_user.first_name = user.POST['first_name']
        new_user.last_name = user.POST['last_name']
        new_user.group = user.POST['group'] 

@csrf_exempt
@require_http_methods(['POST'])        
def check_clocked_in(request):
	clocked_in = request.POST['clocked_in']
	return clocked_in == "True" || clocked_in == "true" 
	       || clocked_in == true
