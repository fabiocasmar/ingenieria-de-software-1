# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0005_auto_20150513_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billetera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('saldo', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=4)),
                ('usuario', models.ForeignKey(to='estacionamientos.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('saldo', models.CharField(max_length=100)),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
                ('establecimiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('saldo', models.CharField(max_length=100)),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='cedulaTipo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cedulaTipo',
        ),
    ]
