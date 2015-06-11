# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20150607_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='apellido',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='cedula',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombre',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
