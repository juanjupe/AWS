# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webjuego', '0005_auto_20171023_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
