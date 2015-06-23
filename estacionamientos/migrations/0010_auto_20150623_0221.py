# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0009_auto_20150622_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='capacidad',
            field=models.ForeignKey(to='estacionamientos.Puestos', default=0),
        ),
    ]
