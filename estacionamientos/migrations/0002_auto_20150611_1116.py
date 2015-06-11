# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelarReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedula', models.CharField(null=True, blank=True, max_length=10)),
                ('inicioReserva', models.DateTimeField(blank=True, null=True)),
                ('finalReserva', models.DateTimeField(blank=True, null=True)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuienReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pago',
            name='cedulaTipo',
        ),
    ]
