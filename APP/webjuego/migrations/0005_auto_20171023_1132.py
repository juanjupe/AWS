# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webjuego', '0004_auto_20171023_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='imagenes/'),
        ),
    ]
