import json
import urllib
import urllib.parse

from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse

from snc_python_api.models import Product


# Create your views here.

def diplom(request):
    Product.objects.create(urlImage="https://kosmetika-proff.ru/upload/iblock/441/p3l16i79jdd6sss16kpzwyavl1on1m1y.png",
                           brand="DOTT.SOLARI COSMETICS olea baobab",
                           name="ШАМПУНЬ ДЛЯ ВОЛОС",
                           description="Шампунь с маслами баобаба и семени льна - идеальное средство для заботы о тонких и подвергнутых химической обработке волосах, а также обеспечивает высококачественный уход за наращенными волосами. "
                                       "Благодаря обилию питательных, увлажняющих компонентов и витаминов он мягко и эффективно очищает пряди и " \
                                       "чувствительную кожу головы, восстанавливает влажность, укрепляет структуру волос и придает им мягкость и " \
                                       "шелковистость. "
                                       "Подходит для ежедневного применения.")
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
    return JsonResponse(results, safe=False)


def getProductWithCondition(request):
    condition = request.GET['condition']
    list = Product.objects.filter(typeProblem=condition)
    results = [ob.as_json() for ob in list]
    return JsonResponse(results, safe=False)


def getSetsHair(request):
    brand = request.GET['brand']
    name = request.GET['name']
    brand_split = brand.split()
    containtShampoo = 'ШАМПУНЬ' in name
    containtSpray = 'СПРЕЙ' in name
    containtBalm = 'БАЛЬЗАМ' in name
    containtConditioner = 'КОНДИЦИОНЕР' in name
    containtMask = 'МАСКА' in name
    list = Product.objects.filter(brand__in=brand_split)
    if containtShampoo:
        listSets = list.filter(~Q(name__icontains='ШАМПУНЬ'))
    if containtSpray:
        listSets = list.filter(~Q(name__icontains='СПРЕЙ'))
    if containtBalm:
        listSets = list.filter(~Q(name__icontains='БАЛЬЗАМ'))
    if containtConditioner:
        listSets = list.filter(~Q(name__icontains='КОНДИЦИОНЕР'))
    if containtMask:
        listSets = list.filter(~Q(name__icontains='МАСКА'))

    results = [ob.as_json() for ob in listSets]
    return JsonResponse(results, safe=False)
