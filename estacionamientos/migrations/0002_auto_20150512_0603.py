# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedulaTipo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('clave', models.CharField(max_length=10)),
                ('saldo', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='propietario',
            field=models.ForeignKey(to='estacionamientos.Usuario'),
            preserve_default=True,
        ),
    ]
