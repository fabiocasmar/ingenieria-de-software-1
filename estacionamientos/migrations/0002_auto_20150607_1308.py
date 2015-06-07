# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumo',
            name='saldo',
            field=models.FloatField(),
        ),
    ]
