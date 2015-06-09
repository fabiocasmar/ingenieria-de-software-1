# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuienReserva',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(null=True, max_length=50, blank=True)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(max_length=10)),
            ],
        ),
    ]
