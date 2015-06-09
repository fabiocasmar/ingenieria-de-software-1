# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0003_remove_pago_cedulatipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='apellido',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='reserva',
            name='cedula',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombre',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]
