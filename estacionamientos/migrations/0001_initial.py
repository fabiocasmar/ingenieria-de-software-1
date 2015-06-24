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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('saldo', models.FloatField()),
                ('pin', models.CharField(null=True, blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='CancelarReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedula', models.CharField(null=True, blank=True, max_length=10)),
                ('inicioReserva', models.DateTimeField(null=True, blank=True)),
                ('finalReserva', models.DateTimeField(null=True, blank=True)),
                ('multa', models.DecimalField(max_digits=256, null=True, decimal_places=2, blank=True)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracionSMS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('saldo', models.FloatField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('flag', models.CharField(null=True, blank=True, max_length=1)),
                ('servicio', models.CharField(null=True, blank=True, max_length=1)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(null=True, blank=True, max_length=30)),
                ('telefono2', models.CharField(null=True, blank=True, max_length=30)),
                ('telefono3', models.CharField(null=True, blank=True, max_length=30)),
                ('email1', models.EmailField(null=True, blank=True, max_length=254)),
                ('email2', models.EmailField(null=True, blank=True, max_length=254)),
                ('horizontedias', models.CharField(max_length=2)),
                ('horizontehoras', models.CharField(max_length=2)),
                ('rif', models.CharField(max_length=12)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('apertura', models.TimeField(null=True, blank=True)),
                ('cierre', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fechaTransaccion', models.DateTimeField()),
                ('cedula', models.CharField(max_length=10)),
                ('tarjetaTipo', models.CharField(max_length=6)),
                ('monto', models.DecimalField(max_digits=256, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(null=True, blank=True, max_length=30)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Puestos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('particular', models.IntegerField(null=True)),
                ('moto', models.IntegerField(null=True)),
                ('carga', models.IntegerField(null=True)),
                ('discapacitado', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuienReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(null=True, max_length=10)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('saldo', models.FloatField()),
                ('fechaTransaccion_vieja', models.DateTimeField()),
                ('fechaTransaccion', models.DateTimeField()),
                ('id_viejo', models.CharField(max_length=10)),
                ('monto_reserva', models.FloatField(null=True, blank=True)),
                ('mensaje', models.CharField(null=True, blank=True, max_length=100)),
                ('billetera', models.ForeignKey(to='estacionamientos.Billetera')),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
                ('cedula', models.CharField(null=True, max_length=10)),
                ('inicioReserva', models.DateTimeField()),
                ('finalReserva', models.DateTimeField()),
                ('movidas', models.FloatField(default=0)),
                ('tipo_puesto', models.CharField(null=True, blank=True, max_length=50)),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Sage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('deduccion', models.DecimalField(max_digits=256, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='TarifaFinDeSemana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tarifa', models.DecimalField(max_digits=20, decimal_places=2)),
                ('tarifa2', models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(null=True, blank=True, max_length=50)),
                ('apellido', models.CharField(null=True, blank=True, max_length=50)),
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
            name='capacidad',
            field=models.ForeignKey(to='estacionamientos.Puestos', default=0),
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='content_type',
            field=models.ForeignKey(null=True, to='contenttypes.ContentType'),
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
