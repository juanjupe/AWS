# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webjuego', '0002_auto_20171016_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(upload_to=b''),
        ),
    ]
