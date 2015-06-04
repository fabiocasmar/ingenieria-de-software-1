# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billetera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('saldo', models.FloatField()),
                ('pin', models.CharField(max_length=4, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracionSMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('saldo', models.CharField(max_length=100)),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(max_length=30, null=True, blank=True)),
                ('telefono2', models.CharField(max_length=30, null=True, blank=True)),
                ('telefono3', models.CharField(max_length=30, null=True, blank=True)),
                ('email1', models.EmailField(max_length=254, null=True, blank=True)),
                ('email2', models.EmailField(max_length=254, null=True, blank=True)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('apertura', models.TimeField(null=True, blank=True)),
                ('cierre', models.TimeField(null=True, blank=True)),
                ('capacidad', models.IntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(null=True, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=256)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50, null=True, blank=True)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaHoraPico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tarifa2', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
                ('inicioEspecial', models.TimeField(null=True, blank=True)),
                ('finEspecial', models.TimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('apellido', models.CharField(max_length=50, null=True, blank=True)),
                ('cedula', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.ForeignKey(to='estacionamientos.Reserva'),
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='propietario',
            field=models.ForeignKey(to='estacionamientos.Propietario'),
        ),
        migrations.AddField(
            model_name='consumo',
            name='establecimiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento'),
        ),
        migrations.AddField(
            model_name='configuracionsms',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento'),
        ),
        migrations.AddField(
            model_name='billetera',
            name='usuario',
            field=models.ForeignKey(to='estacionamientos.Usuario'),
        ),
    ]
