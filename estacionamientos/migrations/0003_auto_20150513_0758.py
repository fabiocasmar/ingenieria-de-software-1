# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20150512_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=120)),
                ('telefono1', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono3', models.CharField(blank=True, max_length=30, null=True)),
                ('email1', models.EmailField(blank=True, max_length=75, null=True)),
                ('email2', models.EmailField(blank=True, max_length=75, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='clave',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='saldo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.TextField(blank=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='email1',
            field=models.EmailField(blank=True, max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='email2',
            field=models.EmailField(blank=True, max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono1',
            field=models.CharField(blank=True, max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono2',
            field=models.CharField(blank=True, max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono3',
            field=models.CharField(blank=True, max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='propietario',
            field=models.ForeignKey(to='estacionamientos.Propietario'),
            preserve_default=True,
        ),
    ]
