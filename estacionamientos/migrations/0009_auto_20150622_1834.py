# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0008_reembolso_id_viejo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puestos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('particular', models.PositiveIntegerField(null=True)),
                ('moto', models.PositiveIntegerField(null=True)),
                ('carga', models.PositiveIntegerField(null=True)),
                ('discapacitado', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='capacidad',
            field=models.ForeignKey(to='estacionamientos.Puestos', default=1),
            preserve_default=False,
        ),
    ]
