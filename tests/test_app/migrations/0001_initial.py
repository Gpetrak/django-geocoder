# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django_geocoder.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('locality', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('administrative_area_level_1', models.CharField(blank=True, max_length=255, null=True)),
                ('administrative_area_level_2', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
            ],
            bases=(models.Model, django_geocoder.mixins.GeoMixin),
        ),
    ]