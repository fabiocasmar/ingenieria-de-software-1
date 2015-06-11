# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_quienreserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='cedulaTipo',
        ),
    ]
