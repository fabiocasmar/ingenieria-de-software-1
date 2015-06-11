# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billetera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('saldo', models.FloatField()),
                ('pin', models.CharField(blank=True, null=True, max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfiguracionSMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(blank=True, null=True, max_length=30)),
                ('telefono2', models.CharField(blank=True, null=True, max_length=30)),
                ('telefono3', models.CharField(blank=True, null=True, max_length=30)),
                ('email1', models.EmailField(blank=True, null=True, max_length=75)),
                ('email2', models.EmailField(blank=True, null=True, max_length=75)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('apertura', models.TimeField(blank=True, null=True)),
                ('cierre', models.TimeField(blank=True, null=True)),
                ('capacidad', models.IntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(null=True, to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(blank=True, null=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(blank=True, null=True, max_length=30)),
                ('email', models.EmailField(blank=True, null=True, max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(blank=True, null=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(blank=True, null=True, max_length=50)),
                ('apellido', models.CharField(blank=True, null=True, max_length=50)),
                ('cedula', models.CharField(null=True, max_length=10)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHoraPico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(blank=True, null=True, max_length=50)),
                ('apellido', models.CharField(blank=True, null=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.ForeignKey(to='estacionamientos.Reserva'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='propietario',
            field=models.ForeignKey(to='estacionamientos.Propietario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consumo',
            name='establecimiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configuracionsms',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billetera',
            name='usuario',
            field=models.ForeignKey(to='estacionamientos.Usuario'),
            preserve_default=True,
        ),
    ]
