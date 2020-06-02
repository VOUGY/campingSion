from django.urls import path
from . import views

urlpatterns = [
    path('location/<int:location_id>/book', views.book, name='book-location'),
    path('book', views.book, name='book'),
    path('thanks', views.thanks, name='thanks')
]
