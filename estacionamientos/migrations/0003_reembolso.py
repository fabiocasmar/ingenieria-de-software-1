# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_consumo_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reembolso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula', models.CharField(max_length=10, null=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
    ]
