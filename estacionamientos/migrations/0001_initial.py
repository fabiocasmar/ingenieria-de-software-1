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
                ('pin', models.CharField(null=True, max_length=4, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CancelarReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedula', models.CharField(null=True, max_length=10, blank=True)),
                ('inicioReserva', models.DateTimeField(null=True, blank=True)),
                ('finalReserva', models.DateTimeField(null=True, blank=True)),
                ('multa', models.DecimalField(null=True, max_digits=256, blank=True, decimal_places=2)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
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
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('flag', models.CharField(null=True, max_length=1, blank=True)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(null=True, max_length=30, blank=True)),
                ('telefono2', models.CharField(null=True, max_length=30, blank=True)),
                ('telefono3', models.CharField(null=True, max_length=30, blank=True)),
                ('email1', models.EmailField(null=True, max_length=254, blank=True)),
                ('email2', models.EmailField(null=True, max_length=254, blank=True)),
                ('horizontedias', models.CharField(max_length=2)),
                ('horizontehoras', models.CharField(max_length=2)),
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
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(max_digits=256, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(null=True, max_length=30, blank=True)),
                ('email', models.EmailField(null=True, max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuienReserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(null=True, max_length=50, blank=True)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(max_length=10)),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('numtarjeta', models.CharField(default=0, max_length=16)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Reembolso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(null=True, max_length=50, blank=True)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(null=True, max_length=10)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('saldo', models.FloatField()),
                ('fechaTransaccion_vieja', models.DateTimeField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('id_viejo', models.CharField(max_length=10)),
                ('monto_reserva', models.FloatField(null=True, blank=True)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(null=True, max_length=50, blank=True)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(null=True, max_length=10)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('movidas', models.FloatField(default=0)),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(null=True, max_digits=10, blank=True, decimal_places=2)),
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
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(null=True, max_digits=10, blank=True, decimal_places=2)),
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
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(null=True, max_digits=10, blank=True, decimal_places=2)),
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
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(null=True, max_digits=10, blank=True, decimal_places=2)),
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
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(null=True, max_digits=10, blank=True, decimal_places=2)),
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
                ('nombre', models.CharField(null=True, max_length=50, blank=True)),
                ('apellido', models.CharField(null=True, max_length=50, blank=True)),
                ('cedula', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.ForeignKey(to='estacionamientos.Reserva', default=0),
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
            model_name='consumo',
            name='reserva',
            field=models.ForeignKey(to='estacionamientos.Reserva', default=0),
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
