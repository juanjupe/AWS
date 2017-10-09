# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webjuego', '0002_auto_20171002_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='juego',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='puntuacione',
        ),
        migrations.AddField(
            model_name='comentario',
            name='juego',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webjuego.Juego'),
        ),
        migrations.AddField(
            model_name='puntuacione',
            name='juego',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webjuego.Juego'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ManyToManyField(default=0, to='webjuego.Usuario'),
        ),
        migrations.RemoveField(
            model_name='puntuacione',
            name='usuario',
        ),
        migrations.AddField(
            model_name='puntuacione',
            name='usuario',
            field=models.ManyToManyField(to='webjuego.Usuario'),
        ),
        migrations.AlterField(
            model_name='puntuacione',
            name='valoracion',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='plataforma',
            name='juego',
            field=models.ManyToManyField(default=0, to='webjuego.Juego'),
        ),
    ]