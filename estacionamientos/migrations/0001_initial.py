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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('saldo', models.FloatField()),
                ('pin', models.CharField(null=True, blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='CancelarReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedula', models.CharField(null=True, blank=True, max_length=10)),
                ('inicioReserva', models.DateTimeField(blank=True, null=True)),
                ('finalReserva', models.DateTimeField(blank=True, null=True)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracionSMS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(null=True, blank=True, max_length=30)),
                ('telefono2', models.CharField(null=True, blank=True, max_length=30)),
                ('telefono3', models.CharField(null=True, blank=True, max_length=30)),
                ('email1', models.EmailField(null=True, blank=True, max_length=254)),
                ('email2', models.EmailField(null=True, blank=True, max_length=254)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('apertura', models.TimeField(blank=True, null=True)),
                ('cierre', models.TimeField(blank=True, null=True)),
                ('capacidad', models.IntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(max_digits=256, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(null=True, blank=True, max_length=30)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='QuienReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10, null=True)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaHora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaHoraPico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaHorayFraccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TarifaMinuto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('inicioEspecial', models.TimeField(blank=True, null=True)),
                ('finEspecial', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
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
            model_name='cancelarreserva',
            name='estacionamiento',
            field=models.ForeignKey(to='estacionamientos.Estacionamiento'),
        ),
        migrations.AddField(
            model_name='billetera',
            name='usuario',
            field=models.ForeignKey(to='estacionamientos.Usuario'),
        ),
    ]
