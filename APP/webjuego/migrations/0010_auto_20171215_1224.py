# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 12:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webjuego', '0009_auto_20171024_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
