from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Tree, SwimmingPool, Location, CampingArea, Building, Booking


def index(request):
    return render(request, 'index.html')


def treesjson(request):
    trees = Tree.objects.all()
    ser = serialize('geojson', trees, geometry_field='geom')
    return HttpResponse(ser)


def swimmingpoolsjson(request):
    swimmingpools = SwimmingPool.objects.all()
    ser = serialize('geojson', swimmingpools, geometry_field='geom')
    return HttpResponse(ser)


def locationsjson(request):
    locations = Location.objects.all().prefetch_related('bookings')
    ser = serialize('geojson', locations, geometry_field='geom')
    return HttpResponse(ser)


def campingareasjson(request):
    campingareas = CampingArea.objects.all()
    ser = serialize('geojson', campingareas, geometry_field='geom')
    return HttpResponse(ser)


def buildingsjson(request):
    buildings = Building.objects.all()
    ser = serialize('geojson', buildings, geometry_field='geom')
    return HttpResponse(ser)


def bookingjson(request):
    booking = Booking.objects.all()
    ser = serialize('geojson', booking, geometry_field='geom')
    return HttpResponse(ser)

