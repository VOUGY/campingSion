from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import SwimmingPool


def index(request):
    return render(request, 'index.html')


def swimmingpoolsjson(request):
    swimmingpools = SwimmingPool.objects.all()
    ser = serialize('geojson', swimmingpools, geometry_field='geom')
    return HttpResponse(ser)


