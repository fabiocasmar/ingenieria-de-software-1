# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_sage'),
    ]

    operations = [
        migrations.AddField(
            model_name='reembolso',
            name='mensaje',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
