# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('comentario', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Creador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patrocinador', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creador', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webjuego.Creador')),
                ('genero', models.ManyToManyField(default=0, to='webjuego.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Puntuacione',
            fields=[
                ('valoracion', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('juego', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webjuego.Juego')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='puntuacione',
            name='usuario',
            field=models.ManyToManyField(to='webjuego.Usuario'),
        ),
        migrations.AddField(
            model_name='juego',
            name='plataforma',
            field=models.ManyToManyField(default=0, to='webjuego.Plataforma'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='juego',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webjuego.Juego'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ManyToManyField(default=0, to='webjuego.Usuario'),
        ),
    ]
