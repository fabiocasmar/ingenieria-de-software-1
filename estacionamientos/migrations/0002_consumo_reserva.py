# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumo',
            name='reserva',
            field=models.ForeignKey(default=0, to='estacionamientos.Reserva'),
        ),
    ]
