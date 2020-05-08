# Generated by Django 3.0.5 on 2020-05-08 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_web', '0002_auto_20200508_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('tel_number', models.CharField(max_length=30)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('busy', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_web.Location')),
            ],
        ),
    ]
