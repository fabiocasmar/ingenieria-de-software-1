# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0012_auto_20150623_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='object_id2',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
