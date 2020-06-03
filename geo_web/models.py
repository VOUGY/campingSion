from django.contrib.gis.db import models


class SwimmingPool(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Location(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=100)
    bookings = models.ManyToManyField('booking.Booking')


class Tree(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.PointField(srid=3857, null=True)
    id = models.BigIntegerField(null=True)


class CampingArea(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=100)

class myCampingArea(CampingArea):
    area = 12

    class Meta:
        proxy = True


class Building(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
