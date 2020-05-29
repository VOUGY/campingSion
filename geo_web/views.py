from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db.models import Q
from .models import Tree, SwimmingPool, Location, CampingArea, Building, Booking
import datetime

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
    locations = Location.objects.all()
    ser = serialize('geojson', locations, geometry_field='geom')
    return HttpResponse(ser)


def freelocationsjson(request):
    today = datetime.date.today()
    locations = Location.objects.filter(Q(bookings__isnull=True) | Q(bookings__date_start__gt=today, bookings__date_end__lt=today))
    # locations = Location.get(1)
    ser = serialize('geojson', locations, geometry_field='geom')
    return HttpResponse(ser)


def busylocationsjson(request):
    today = datetime.date.today()
    locations = Location.objects.filter(bookings__date_start__lt=today).filter(bookings__date_end__gt=today)
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

