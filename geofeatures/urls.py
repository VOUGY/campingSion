from django.urls import path
from . import views

urlpatterns = [
    path('gf', views.index, name='index'),
]