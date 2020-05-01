from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Piciine


def index(request):
    return render(request, 'index.html')


def piciinejson(request):
    picine = Piciine.objects.all()
    ser = serialize('geojson', picine, geometry_field='geom')
    return HttpResponse(ser)


