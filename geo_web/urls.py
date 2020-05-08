from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/geojson/swimmingpools.json', views.swimmingpoolsjson, name='swimmingpoolsjson'),
]