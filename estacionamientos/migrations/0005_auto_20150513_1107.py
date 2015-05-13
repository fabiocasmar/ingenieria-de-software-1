# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0004_auto_20150513_0758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propietario',
            old_name='email1',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='propietario',
            old_name='telefono1',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='email1',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='telefono1',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='telefono2',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='telefono3',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono2',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono3',
        ),
        migrations.AddField(
            model_name='propietario',
            name='apellido',
            field=models.CharField(null=True, max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
