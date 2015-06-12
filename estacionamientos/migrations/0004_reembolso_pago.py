# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0003_reembolso'),
    ]

    operations = [
        migrations.AddField(
            model_name='reembolso',
            name='pago',
            field=models.ForeignKey(to='estacionamientos.Pago', default=0),
        ),
    ]
