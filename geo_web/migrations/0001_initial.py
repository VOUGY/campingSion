# Generated by Django 3.0.5 on 2020-05-08 08:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id_0', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CampingArea',
            fields=[
                ('id_0', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id_0', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SwimmingPool',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id_0', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('id', models.BigIntegerField()),
            ],
        ),
    ]
