# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0005_remove_reembolso_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='numtarjeta',
            field=models.CharField(default=0, max_length=16),
        ),
    ]
