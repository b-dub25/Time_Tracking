def get_obj_or_none(obj, kwargs):
    try:
        return obj.objects.get(**kwargs)
    except:
        return None
