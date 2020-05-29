from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/geojson/trees.json', views.treesjson, name='treesjson'),
    path('/geojson/swimmingpools.json', views.swimmingpoolsjson, name='swimmingpoolsjson'),
    path('/geojson/locations.json', views.locationsjson, name='locationsjson'),
    path('/geojson/free-locations.json', views.freelocationsjson, name='freelocationsjson'),
    path('/geojson/busy-locations.json', views.busylocationsjson, name='busylocationsjson'),
    path('/geojson/campingareas.json', views.campingareasjson, name='campingareasjson'),
    path('/geojson/buildings.json', views.buildingsjson, name='buildingsjson'),
    path('/geojson/booking.json', views.bookingjson, name='bookingjson')
]
