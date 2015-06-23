# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0010_auto_20150623_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='tipo_puesto',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
