from django.contrib.gis.db import models


class Piciine(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326, null=True)

    class Meta:
        db_table = "Piciine"
