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

    @property
    def add_area(self):
        # area = ("%.0f" % object.geom.area)
        area = 12
        return area


# class MyCampingArea(CampingArea):
#     myField = models.PositiveIntegerField(null=True)
#
#     class Meta:
#         proxy = True
#
#     def add_area(self):
#         # area = ("%.0f" % object.geom.area)
#         area = 12
#         return area



class Building(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
