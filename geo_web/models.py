from django.contrib.gis.db import models


class SwimmingPool(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)


class Location(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField(null=True)


class Tree(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField(null=True)


class CampingArea(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField(null=True)


class Building(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField(null=True)

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    tel_number = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    busy = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)



