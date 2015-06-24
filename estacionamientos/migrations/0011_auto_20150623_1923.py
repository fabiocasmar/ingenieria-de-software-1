# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0010_auto_20150623_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninguno',
            old_name='inicioEspecialFerdiado',
            new_name='inicioEspecialFeriado',
        ),
        migrations.RenameField(
            model_name='tarifafindesemana',
            old_name='inicioEspecialFerdiado',
            new_name='inicioEspecialFeriado',
        ),
        migrations.RenameField(
            model_name='tarifahora',
            old_name='inicioEspecialFerdiado',
            new_name='inicioEspecialFeriado',
        ),
        migrations.RenameField(
            model_name='tarifahorapico',
            old_name='inicioEspecialFerdiado',
            new_name='inicioEspecialFeriado',
        ),
        migrations.RenameField(
            model_name='tarifahorayfraccion',
            old_name='inicioEspecialFerdiado',
            new_name='inicioEspecialFeriado',
        ),
        migrations.RenameField(
            model_name='tarifaminuto',
            old_name='inicioEspecialFerdiado',
            new_name='inicioEspecialFeriado',
        ),
    ]
