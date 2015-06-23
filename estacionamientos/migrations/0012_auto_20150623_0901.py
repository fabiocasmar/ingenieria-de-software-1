# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0011_reserva_tipo_puesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puestos',
            name='carga',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='discapacitado',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='moto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='puestos',
            name='particular',
            field=models.IntegerField(null=True),
        ),
    ]
