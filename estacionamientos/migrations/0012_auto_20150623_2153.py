# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0011_auto_20150623_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninguno',
            name='tarifa',
            field=models.DecimalField(max_digits=20, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tarifafindesemana',
            name='tarifa',
            field=models.DecimalField(max_digits=20, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tarifahora',
            name='tarifa',
            field=models.DecimalField(max_digits=20, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tarifahorapico',
            name='tarifa',
            field=models.DecimalField(max_digits=20, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tarifahorayfraccion',
            name='tarifa',
            field=models.DecimalField(max_digits=20, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tarifaminuto',
            name='tarifa',
            field=models.DecimalField(max_digits=20, null=True, decimal_places=2),
        ),
    ]
