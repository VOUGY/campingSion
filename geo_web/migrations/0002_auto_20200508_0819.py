# Generated by Django 3.0.5 on 2020-05-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campingarea',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='id',
            field=models.BigIntegerField(null=True),
        ),
    ]
