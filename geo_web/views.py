from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db.models import Q
from .models import Tree, SwimmingPool, Location, CampingArea, Building
from geofeatures.area_features import get_area_object, get_dist_rest, \
    get_dist_swimPool, is_any_tree, get_dist_shop
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

def geofeatures(request, id):
    surf = get_area_object('location', id)
    distRest = get_dist_rest('location', id)
    swimPoolDist = get_dist_swimPool('location', id)
    anyTree = is_any_tree('location', id)
    distShop = get_dist_shop('location', id)
    context = {
        'area': surf,
        'distRest': distRest,
        'swimPoolDist':swimPoolDist,
        'anyTree':anyTree,
        'distShop':distShop
    }
    return render(request, 'geofeatures.html', context)


# def view(request, id):
#     location_area = Location.objects.get(id_0=id).geom.area
#     render_template_to_response("index.html", {"location_area": location_area, …})

def buildingsjson(request):
    buildings = Building.objects.all()
    ser = serialize('geojson', buildings, geometry_field='geom')
    return HttpResponse(ser)

