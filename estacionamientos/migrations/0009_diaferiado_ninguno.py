# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0008_reembolso_id_viejo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaFeriado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('dia', models.PositiveIntegerField(null=True)),
                ('mes', models.PositiveIntegerField(null=True)),
                ('descripcion', models.CharField(null=True, max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ninguno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=10)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
