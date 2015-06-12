# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0006_recarga_numtarjeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='reembolso',
            name='fechaTransaccion_vieja',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 5, 23, 14, 747105)),
            preserve_default=False,
        ),
    ]
