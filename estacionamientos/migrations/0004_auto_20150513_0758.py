# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0003_auto_20150513_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='direccion',
            field=models.TextField(blank=True, max_length=120),
            preserve_default=True,
        ),
    ]
