# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billetera',
            name='pin',
            field=models.CharField(null=True, max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='billetera',
            name='saldo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
