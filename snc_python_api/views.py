import json

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from snc_python_api.models import Product


# Create your views here.

def diplom(request):
    Product.objects.create(name="table_2", cost=2300)
    return JsonResponse({'home': 'bar'})


def diplom_1(request):
    list = Product.objects.all()
    # [print(ob) for ob in list]
    # print(list)
    # leads_as_json = serializers.serialize('json', list)
    # return HttpResponse(leads_as_json, content_type='application/json')
    results = [ob.as_json() for ob in list]
    return HttpResponse(json.dumps(results), content_type="application/json")


def diplom_2(request):
    list = Product.objects.all()
    # [print(ob) for ob in list]
    # print(list)
    # leads_as_json = serializers.serialize('json', list)
    # return HttpResponse(leads_as_json, content_type='application/json')
    results = [ob.as_json() for ob in list]
    return JsonResponse({'malina': 'puk', 'foo': results})


def diplom_3(request):
    list = Product.objects.all()
    # [print(ob) for ob in list]
    # print(list)
    # leads_as_json = serializers.serialize('json', list)
    # return HttpResponse(leads_as_json, content_type='application/json')
    results = [ob.as_json() for ob in list]
    return JsonResponse(results)
