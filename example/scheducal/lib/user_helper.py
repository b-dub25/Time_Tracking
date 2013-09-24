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
