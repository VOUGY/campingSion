from django.shortcuts import render
from . import area_features


def index(request):
    pools_areas = area_features.get_area_objects('pool')
    building_areas = area_features.get_area_objects('building')
    area_areas = area_features.get_area_objects('area')
    locations_areas = area_features.get_area_objects('location')

    context = {
        'pools_areas': pools_areas,
        'building_areas' : building_areas,
        'area_areas' : area_areas,
        'locations_areas' : locations_areas
    }

    return render(request, 'geofeatures.html', context)