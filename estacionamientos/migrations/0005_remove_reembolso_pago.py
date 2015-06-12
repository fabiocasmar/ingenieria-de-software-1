# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0004_reembolso_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reembolso',
            name='pago',
        ),
    ]
