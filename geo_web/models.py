from django.contrib.gis.db import models


class SwimmingPool(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)


class Location(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField()


class Tree(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField()


class CampingArea(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField()


class Building(models.Model):
    id_0 = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    id = models.BigIntegerField()
