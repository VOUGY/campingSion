# Generated by Django 3.0.5 on 2020-05-31 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_web', '0006_auto_20200529_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='busy',
        ),
    ]
