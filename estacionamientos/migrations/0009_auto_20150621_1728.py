# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0008_reembolso_id_viejo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelarreserva',
            name='multa',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=256, blank=True),
        ),
        migrations.AddField(
            model_name='reembolso',
            name='monto_reserva',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
