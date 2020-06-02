from django.db import models


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    tel_number = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
