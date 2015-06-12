# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0007_reembolso_fechatransaccion_vieja'),
    ]

    operations = [
        migrations.AddField(
            model_name='reembolso',
            name='id_viejo',
            field=models.CharField(default=datetime.datetime(2015, 6, 12, 5, 30, 58, 866112), max_length=10),
            preserve_default=False,
        ),
    ]
