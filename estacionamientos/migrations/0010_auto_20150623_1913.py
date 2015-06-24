# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0009_diaferiado_ninguno'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninguno',
            name='finEspecialFeriado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ninguno',
            name='inicioEspecialFerdiado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ninguno',
            name='tarifa2Feriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='ninguno',
            name='tarifaFeriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='tarifafindesemana',
            name='finEspecialFeriado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifafindesemana',
            name='inicioEspecialFerdiado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifafindesemana',
            name='tarifa2Feriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='tarifafindesemana',
            name='tarifaFeriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='finEspecialFeriado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='inicioEspecialFerdiado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='tarifa2Feriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='tarifahora',
            name='tarifaFeriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='tarifahorapico',
            name='finEspecialFeriado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifahorapico',
            name='inicioEspecialFerdiado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifahorapico',
            name='tarifa2Feriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='tarifahorapico',
            name='tarifaFeriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='finEspecialFeriado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='inicioEspecialFerdiado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='tarifa2Feriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='tarifahorayfraccion',
            name='tarifaFeriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='finEspecialFeriado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='inicioEspecialFerdiado',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='tarifa2Feriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='tarifaminuto',
            name='tarifaFeriado',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=20),
        ),
    ]
