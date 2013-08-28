from django.http import HttpResponse
from scheducal.models import Category
from scheducal.lib.obj_helper import get_obj_or_none
from scheducal.forms.category import CategoryForm
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(['GET'])
def category_list(request):
    categories = Category.objects.all()
    data = [category.to_dict() for category in categories]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@csrf_exempt
@require_http_methods(['POST'])
def category_add(request):
    post = request.POST.copy()
    if post['is_project'] == 'true':
        post['is_project'] = True
    if post['is_project'] == 'false':
        post['is_project'] = False
    print post
    form = CategoryForm(post)
    if form.is_valid():
        name = form.cleaned_data['name']
        is_project = request.POST['is_project']
        args = {'name': name, 'is_project' : is_project}
    
        # If object exists, duplicate. 
        if get_obj_or_none(Category, args):
            return HttpResponse(status=409)

        category = Category(name=name, is_project=is_project)
        try:
            category.save()
        # Unexpected Error
        except:
            return HttpResponse(status=400)
        return HttpResponse(status=201)
    # Form not valid, invalid data.
    return HttpResponse(status=400)
        

@require_http_methods(['GET'])
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    data = simplejson.dumps(category.to_dict())
    return HttpResponse(data, mimetype='application/json')
