# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0013_estacionamiento_object_id2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamiento',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='estacionamiento',
            name='object_id2',
        ),
        migrations.AddField(
            model_name='ninguno',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento', default=None),
        ),
        migrations.AddField(
            model_name='tarifafindesemana',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento', default=None),
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento', default=None),
        ),
        migrations.AddField(
            model_name='tarifahorapico',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento', default=None),
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento', default=None),
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento', default=None),
        ),
    ]
